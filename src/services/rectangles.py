import json

from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.decorators import file_path_required
from src.models.rectangles import Rect
from src.schemas.rectangles import RectSchema
from src.services.abstract import FigureService


class RectService(FigureService):

    def create(
        self,
        x_left_up: int,
        y_left_up: int,
        x_right_down: int,
        y_right_down: int,
    ):
        """Создать прямоугольник в двухмерной плоскости"""
        with get_session_for_cli() as db:
            rect = Rect(
                x_left_up=x_left_up,
                y_left_up=y_left_up,
                x_right_down=x_right_down,
                y_right_down=y_right_down,
            )
            if rect.x_left_up >= rect.x_right_down or rect.y_left_up <= rect.y_right_down:
                raise ValueError
            db.add(rect)
            db.commit()
            db.refresh(rect)
            print(f"""
            Вы создали прямоугольник!
            левый верхний угол - x = {rect.x_left_up}, y = {rect.y_left_up}
            правый нижний угол - x = {rect.x_right_down}, y = {rect.y_right_down}
            """)
            return rect

    def delete(self, id_rect: int):
        """Удалить прямоугольник"""
        with get_session_for_cli() as db:
            rect = db.query(Rect).filter(Rect.id == id_rect).first()
            if rect:
                db.delete(rect)
                db.commit()
                print(f"Прямоугольник с id - {id_rect} удален")
                return {"message": f"Прямоугольник с id - {id_rect} удален"}
            else:
                print(f"Прямоугольник с id - {id_rect} не найден")
                return {"error": f"Прямоугольник с id - {id_rect} не найден"}

    def show_figures(self):
        """Показать все прямоугольники"""
        with get_session_for_cli() as db:
            query = select(Rect)
            rects = db.execute(query).scalars().all()
            schemas = [RectSchema.from_orm(rect) for rect in rects]
            for s in schemas:
                print(f"""
            id - {s.id}
            левый верхний угол - x = {s.x_left_up}, y = {s.y_left_up}
            правый нижний угол - x = {s.x_right_down}, y = {s.y_right_down}
            _________________
            """)

    def return_coordinates(self):
        """Возвращает все координаты прямоугольников"""
        with get_session_for_cli() as db:
            query = select(Rect)
            rects = db.execute(query).scalars().all()
            schemas = [RectSchema.from_orm(rect) for rect in rects]
            coordinates = [
                {
                    "id": s.id,
                    "x_left_up": s.x_left_up,
                    "y_left_up": s.y_left_up,
                    "x_right_down": s.x_right_down,
                    "y_right_down": s.y_right_down,
                }
                for s in schemas
            ]
            return coordinates

    @file_path_required()
    def save_to_json(self, path: str, name_figure: str):
        """Записывает все фигуры в json файл"""
        data = self.return_coordinates()
        with open(path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False)
            print("Данные успешно записаны.")

    def load_from_json(self, path: str):
        """Получает все фигуры из json файла"""
        try:
            with open(path, "r", encoding="UTF-8") as file:
                data = json.load(file)
                rects = [RectSchema.model_validate(rect) for rect in data]
                print("Данные прямоугольников из файла:")
                for r in rects:
                    print(f"""
                                id - {r.id}
                                левый верхний угол - x = {r.x_left_up}, y = {r.y_left_up}
                                правый нижний угол - x = {r.x_right_down}, y = {r.y_right_down}
                                _________________
                                """)
        except FileNotFoundError:
            print(f"Файл {path} не найден.")

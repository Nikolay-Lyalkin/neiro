import json

from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.decorators import file_path_required
from src.models.ovals import Oval
from src.schemas.ovals import OvalSchema
from src.services.abstract import FigureService


class OvalService(FigureService):

    def create(
        self,
        x_center: int,
        y_center: int,
        x_radius: int,
        y_radius: int,
    ):
        """Создать овал в двухмерной плоскости"""
        with get_session_for_cli() as db:
            oval = Oval(
                x_center=x_center,
                y_center=y_center,
                x_radius=x_radius,
                y_radius=y_radius,
            )
            if oval.x_radius <= 0 or oval.y_radius <= 0:
                raise ValueError
            db.add(oval)
            db.commit()
            db.refresh(oval)
            print(f"""
            Вы создали квадрат!
            центр овала - x = {oval.x_center}, y = {oval.y_center}
            радиус по оси - x = {oval.x_center}, y = {oval.radius_y}
            """)
            return oval

    def delete(self, id_oval: int):
        """Удалить овал"""
        with get_session_for_cli() as db:
            oval = db.query(Oval).filter(Oval.id == id_oval).first()
            if oval:
                db.delete(oval)
                db.commit()
                print(f"Квадрат с id - {id_oval} удален")
                return {"message": f"Квадрат с id - {id_oval} удален"}
            else:
                print(f"Квадрат с id - {id_oval} не найден")
                return {"error": f"Квадрат с id - {id_oval} не найден"}

    def show_figures(self):
        """Показать все овалы"""
        with get_session_for_cli() as db:
            query = select(Oval)
            ovals = db.execute(query).scalars().all()
            schemas = [OvalSchema.from_orm(oval) for oval in ovals]
            for s in schemas:
                print(f"""
            id - {s.id}
            центр овала - x = {s.x_center}, y = {s.y_center}
            радиус по оси - x = {s.x_center}, y = {s.radius_y}
            _________________
            """)

    def return_coordinates(self):
        """Возвращает все координаты овалов в словаре"""
        with get_session_for_cli() as db:
            query = select(Oval)
            ovals = db.execute(query).scalars().all()
            schemas = [OvalSchema.from_orm(oval) for oval in ovals]
            coordinates = [
                {
                    "id": s.id,
                    "x_center": s.x_center,
                    "y_center": s.y_center,
                    "x_radius": s.x_radius,
                    "y_radius": s.y_radius,
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
                ovals = [OvalSchema.model_validate(oval) for oval in data]
                for o in ovals:
                    print(f"""
                                id - {o.id}
                                центр овала - x = {o.x_center}, y = {o.y_center}
                                радиус по оси - x = {o.x_center}, y = {o.radius_y}
                                _________________
                                """)
        except FileNotFoundError:
            print(f"Файл {path} не найден.")
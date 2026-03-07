import json

from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.decorators import file_path_required
from src.models.circles import Circle
from src.schemas.circles import CircleSchema
from src.services.abstract import FigureService


class CircleService(FigureService):

    def create(self, x: int, y: int, radius: int):
        """Создать круг в двухмерной плоскости"""
        with get_session_for_cli() as db:
            circle = Circle(x=x, y=y, radius=radius)
            if circle.radius <= 0:
                raise ValueError
            db.add(circle)
            db.commit()
            db.refresh(circle)
            print(f"""
                        Вы создали круг!
                        центр круга - x = {circle.x}, y = {circle.y}
                        радиус - {circle.radius}
                        """)
            return circle

    def delete(self, id_circle: int):
        """Удалить круг"""
        with get_session_for_cli() as db:
            circle = db.query(Circle).filter(Circle.id == id_circle).first()
            if circle:
                db.delete(circle)
                db.commit()
                print(f"Круг с id - {id_circle} удален")
                return {"message": f"Круг с id - {id_circle} удален"}
            else:
                print(f"Круг с id - {id_circle} не найден")
                return {"error": f"Круг с id - {id_circle} не найден"}

    def show_figures(self):
        """Показать все круги"""
        with get_session_for_cli() as db:
            query = select(Circle)
            circles = db.execute(query).scalars().all()
            schemas = [CircleSchema.from_orm(circle) for circle in circles]
            for s in schemas:
                print(f"""
                    id - {s.id}
                    центр круга - x = {s.x}, y = {s.y}
                    радиус - {s.radius}
                    _________________
                    """)

    def return_coordinates(self):
        """Возвращает координаты всех кругов"""
        with get_session_for_cli() as db:
            query = select(Circle)
            circles = db.execute(query).scalars().all()
            schemas = [CircleSchema.from_orm(circle) for circle in circles]
            coordinates = [{"id": c.id, "x": c.x, "y": c.y, "radius": c.radius} for c in schemas]
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
                circles = [CircleSchema.model_validate(circle) for circle in data]
                print("Данные кругов из файла:")
                for c in circles:
                    print(f"""
                                        id - {c.id}
                                        центр круга - x = {c.x}, y = {c.y}
                                        радиус - {c.radius}
                                        _________________
                                        """)
        except FileNotFoundError:
            print(f"Файл {path} не найден.")

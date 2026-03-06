from sqlalchemy import select

from src.db.postgres import get_session_for_cli
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
            coordinates = [{"id": c.id, "x": c.x, "y": c.y, "radius": c.radius} for c in schemas]
            for s in schemas:
                print(f"""
                    id - {s.id}
                    центр круга - x = {s.x}, y = {s.y}
                    радиус - {s.radius}
                    _________________
                    """)
            return coordinates

from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.models.points import Point
from src.schemas.point import PointSchema
from src.services.abstract import FigureService


class PointService(FigureService):

    def create(self, x, y):
        """Создать точку в двухмерной плоскости"""
        with get_session_for_cli() as db:
            point = Point(x=x, y=y)
            db.add(point)
            db.commit()
            db.refresh(point)
            print(f"""
            Вы создали точку!
            координаты - x = {point.x}, y = {point.y}
            """)
            return point

    def delete(self, id_point: int):
        """Удалить точку"""
        with get_session_for_cli() as db:
            point = db.query(Point).filter(Point.id == id_point).first()
            if point:
                db.delete(point)
                db.commit()
                print(f"Точка с id - {id_point} удалена")
                return {"message": f"Точка с id - {id_point} удалена"}
            else:
                print(f"Точка с id - {id_point} не найдена")
                return {"error": f"Точка с id - {id_point} не найдена"}

    def show_figures(self):
        """Показать все точки"""
        with get_session_for_cli() as db:
            query = select(Point)
            points = db.execute(query).scalars().all()
            schemas = [PointSchema.from_orm(point) for point in points]
            coordinates = [{"id": p.id, "x": p.x, "y": p.y} for p in schemas]
            for s in schemas:
                print(f"""
                id - {s.id}
                координаты - x = {s.x}, y = {s.y}
                _________________
                """)
            return coordinates

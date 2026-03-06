from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.models.squares import Square
from src.schemas.squares import SquareSchema
from src.services.abstract import FigureService


class SquareService(FigureService):

    def create(
        self,
        x_left_up: int,
        y_left_up: int,
        x_left_down: int,
        y_left_down: int,
        side: int,
    ):
        """Создать квадрат в двухмерной плоскости"""
        with get_session_for_cli() as db:
            square = Square(
                x_left_up=x_left_up,
                y_left_up=y_left_up,
                x_left_down=x_left_down,
                y_left_down=y_left_down,
                side=side,
            )
            if square.side <= 0:
                raise ValueError
            db.add(square)
            db.commit()
            db.refresh(square)
            print(f"""
            Вы создали квадрат!
            левый верхний угол - x = {square.x_left_up}, y = {square.y_left_up}
            левый нижний угол - x = {square.x_left_down}, y = {square.y_left_down}
            длина стороны - {square.side}
            """)
            return square

    def delete(self, id_square: int):
        """Удалить квадрат"""
        with get_session_for_cli() as db:
            square = db.query(Square).filter(Square.id == id_square).first()
            if square:
                db.delete(square)
                db.commit()
                print(f"Квадрат с id - {id_square} удален")
                return {"message": f"Квадрат с id - {id_square} удален"}
            else:
                print(f"Квадрат с id - {id_square} не найден")
                return {"error": f"Квадрат с id - {id_square} не найден"}

    def show_figures(self):
        """Показать все квадраты"""
        with get_session_for_cli() as db:
            query = select(Square)
            squares = db.execute(query).scalars().all()
            schemas = [SquareSchema.from_orm(square) for square in squares]
            coordinates = [
                {
                    "id": s.id,
                    "x_left_up": s.x_left_up,
                    "y_left_up": s.y_left_up,
                    "x_left_down": s.x_left_down,
                    "y_left_down": s.y_left_down,
                    "side": s.side,
                }
                for s in schemas
            ]
            for s in schemas:
                print(f"""
            id - {s.id}
            левый верхний угол - x = {s.x_left_up}, y = {s.y_left_up}
            левый нижний угол - x = {s.x_left_down}, y = {s.y_left_down}
            длина стороны - {s.side}
            _________________
            """)
            return coordinates

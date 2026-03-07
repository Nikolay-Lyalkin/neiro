import json

from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.decorators import file_path_required
from src.models.lines import Line
from src.schemas.lines import LineSchema
from src.services.abstract import FigureService


class LineService(FigureService):

    def create(self, x_left: int, y_left: int, x_right: int, y_right: int, length: int):
        """Создать отрезок в двухмерной плоскости"""
        with get_session_for_cli() as db:
            line = Line(
                x_left=x_left,
                y_left=y_left,
                x_right=x_right,
                y_right=y_right,
                length=length,
            )
            db.add(line)
            db.commit()
            db.refresh(line)
            print(f"""
            Вы создали отрезок!
            начало отрезка - x = {line.x_left}, y = {line.y_left}
            конец отрезка - x = {line.x_right}, y = {line.y_right}
            длина - {line.length}
            """)
            return line

    def delete(self, id_line: int):
        """Удалить отрезок"""
        with get_session_for_cli() as db:
            line = db.query(Line).filter(Line.id == id_line).first()
            if line:
                db.delete(line)
                db.commit()
                print(f"Отрезок с id - {id_line} удален")
                return {"message": f"Отрезок с id - {id_line} удален"}
            else:
                print(f"Отрезок с id - {id_line} не найден")
                return {"error": f"Отрезок с id - {id_line} не найден"}

    def show_figures(self):
        """Показать все отрезки"""
        with get_session_for_cli() as db:
            query = select(Line)
            lines = db.execute(query).scalars().all()
            schemas = [LineSchema.from_orm(line) for line in lines]
            for s in schemas:
                print(f"""
            id - {s.id}
            начало отрезка - x = {s.x_left}, y = {s.y_left}
            конец отрезка - x = {s.x_right}, y = {s.y_right}
            длина - {s.length}
            _________________
            """)

    def return_coordinates(self):
        """Возвращает координаты всех фигур"""
        with get_session_for_cli() as db:
            query = select(Line)
            lines = db.execute(query).scalars().all()
            schemas = [LineSchema.from_orm(line) for line in lines]
            coordinates = [
                {
                    "id": l.id,
                    "x_left": l.x_left,
                    "y_left": l.y_left,
                    "x_right": l.x_right,
                    "y_right": l.y_right,
                    "length": l.length,
                }
                for l in schemas
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
                lines = [LineSchema.model_validate(line) for line in data]
                for l in lines:
                    print(f"""
                                id - {l.id}
                                начало отрезка - x = {l.x_left}, y = {l.y_left}
                                конец отрезка - x = {l.x_right}, y = {l.y_right}
                                длина - {l.length}
                                _________________
                                """)
        except FileNotFoundError:
            print(f"Файл {path} не найден.")

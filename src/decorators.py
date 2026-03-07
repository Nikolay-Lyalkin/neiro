import os
from functools import wraps
from typing import Callable

from sqlalchemy import select

from src.db.postgres import get_session_for_cli
from src.models.file_paths import FilePath


def file_path_required():
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            path = kwargs.get("path")
            name_figure = kwargs.get("name_figure")
            with get_session_for_cli() as db:
                query = select(FilePath).where(FilePath.name_file == path)
                figure = db.execute(query).scalar_one_or_none()
                if figure:
                    if figure.name_figure != name_figure:
                        print(
                            f"Ошибка! Вы пытаетесь добавить в файл фигуру - {name_figure}, но там уже сохранена фигура "
                            f"- {figure.name_figure}"
                        )
                        return None
                    elif figure.name_figure == name_figure:
                        return func(*args, **kwargs)
                file_path = FilePath(name_figure=name_figure, name_file=path, abspath=os.path.abspath(path))
                db.add(file_path)
                db.commit()
                db.refresh(file_path)
                return func(*args, **kwargs)

        return wrapper

    return decorator

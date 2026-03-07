from sqlalchemy import Column, Integer, String, Text

from src.models.points import Base


class FilePath(Base):
    __tablename__ = "file_path"

    id = Column(Integer, primary_key=True)
    name_figure = Column(String(255))
    name_file = Column(String(255))
    abspath = Column(Text)

from sqlalchemy import Column, Integer

from src.models.points import Base


class Line(Base):
    __tablename__ = "lines"

    id = Column(Integer, primary_key=True)
    x_left = Column(Integer, nullable=False)
    y_left = Column(Integer, nullable=False)
    x_right = Column(Integer, nullable=False)
    y_right = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)

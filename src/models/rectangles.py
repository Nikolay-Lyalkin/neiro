from sqlalchemy import Column, Integer

from src.models.points import Base


class Rect(Base):
    __tablename__ = "rectangles"

    id = Column(Integer, primary_key=True)
    x_left_up = Column(Integer, nullable=False)
    y_left_up = Column(Integer, nullable=False)
    x_right_down = Column(Integer, nullable=False)
    y_right_down = Column(Integer, nullable=False)

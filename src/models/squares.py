from sqlalchemy import Column, Integer

from src.models.points import Base


class Square(Base):
    __tablename__ = "squares"

    id = Column(Integer, primary_key=True)
    x_left_up = Column(Integer, nullable=False)
    y_left_up = Column(Integer, nullable=False)
    x_left_down = Column(Integer, nullable=False)
    y_left_down = Column(Integer, nullable=False)
    side = Column(Integer, nullable=False)

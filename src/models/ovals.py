from sqlalchemy import Column, Integer

from src.models.points import Base


class Oval(Base):
    __tablename__ = "ovals"

    id = Column(Integer, primary_key=True)
    x_center = Column(Integer, nullable=False)
    y_center = Column(Integer, nullable=False)
    radius_x = Column(Integer, nullable=False)
    radius_y = Column(Integer, nullable=False)
from sqlalchemy import Column, Integer

from src.models.points import Base


class Circle(Base):
    __tablename__ = "circles"

    id = Column(Integer, primary_key=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    radius = Column(Integer, nullable=False)

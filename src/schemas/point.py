from pydantic import BaseModel, ConfigDict


class PointSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    x: int
    y: int

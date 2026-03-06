from pydantic import BaseModel, ConfigDict


class CircleSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    x: int
    y: int
    radius: int

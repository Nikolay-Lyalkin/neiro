from pydantic import BaseModel, ConfigDict


class SquareSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    x_left_up: int
    y_left_up: int
    x_left_down: int
    y_left_down: int
    side: int

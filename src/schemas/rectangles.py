from pydantic import BaseModel, ConfigDict


class RectSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    x_left_up: int
    y_left_up: int
    x_right_down: int
    y_right_down: int

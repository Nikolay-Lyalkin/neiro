from pydantic import BaseModel, ConfigDict


class LineSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    x_left: int
    y_left: int
    x_right: int
    y_right: int
    length: int

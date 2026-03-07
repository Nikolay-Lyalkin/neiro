from pydantic import BaseModel, ConfigDict


class OvalSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    x_center: int
    y_center: int
    x_radius: int
    y_radius: int

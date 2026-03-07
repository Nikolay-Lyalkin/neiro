from pydantic import BaseModel, ConfigDict


class LineSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name_figure: str
    name_file: str
    abspath: str

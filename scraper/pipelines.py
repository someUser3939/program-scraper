from pydantic import BaseModel, Field
from main import get_value


class DataModel(BaseModel):
    title: str = Field(..., description="The title of the series")
    year: str = Field(..., description="The year of release")
    rating: str = Field(..., description="The rating of the series")
    description: str = Field(..., description="The description of the series")

all_info = DataModel(**get_value) # type: ignore

# data = DataModel(**get_value)

data = all_info.model_dump_json() # type: ignore
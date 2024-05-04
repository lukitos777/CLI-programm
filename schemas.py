from pydantic import BaseModel, Field
from typing import Literal

#schemas are used for validation queries
#if entered data will not be valid
#then will be raisen validation error

class Add_Data(BaseModel):
    category: Literal['Расход', 'Доход']
    price: int = Field(min=1)
    desc: str = Field(min_length=3, max_length=75)

class Get_Data_By_ID(BaseModel):
    ID: int = Field(min=1)
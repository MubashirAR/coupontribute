from typing import Optional
from pydantic import BaseModel

class RestaurantBase(BaseModel):
    name: str

class RestaurantCreate(RestaurantBase):
    pass


class Restaurant(RestaurantBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

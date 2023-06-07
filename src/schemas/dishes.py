from pydantic import BaseModel, conint
from typing import List, Optional


class DishesInfo(BaseModel):
    """Базовая схема для позиций в меню"""

    id: int
    name: str
    weight: conint(gt=0)
    description: str
    subcategory_id: int
    price: conint(gt=0)
    is_active: bool

# todo фото

    class Config:
        orm_mode = True


class CreateDishSchema(BaseModel):
    """Схема для создания item"""

    name: str
    weight: conint(gt=0)
    description: str
    is_active: bool = True
    subcategory_id: int
    price: conint(gt=0)

    class Config:
        orm_mode = True


class UpdateDishSchema(BaseModel):
    """Схема для обновления item"""

    name: str
    weight: conint(gt=0)
    description: str
    is_active: bool
    subcategory_id: int
    price: conint(gt=0)

    class Config:
        orm_mode = True








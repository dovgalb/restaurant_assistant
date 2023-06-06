from pydantic import BaseModel
from typing import List, Optional


class DishesInfo(BaseModel):
    """Базовая схема для позиций в меню"""

    id: int
    name: str
    weight: int
    description: str
    is_active: bool
    # price: int

    class Config:
        orm_mode = True


class CreateDishSchema(BaseModel):
    """Схема для создания item"""

    name: str
    weight: int
    description: str
    is_active: bool = True
    # price: int

    class Config:
        orm_mode = True


class UpdateDishSchema(BaseModel):
    """Схема для обновления item"""

    name: str
    weight: int
    description: str
    is_active: bool
    # price: int

    class Config:
        orm_mode = True








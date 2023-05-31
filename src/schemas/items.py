from pydantic import BaseModel
from typing import List, Optional


# class CompoundInfo(BaseModel):
#     id: int


class ItemsInfo(BaseModel):
    """Базовая схема для позиций в меню"""

    id: int
    name: str
    weight: int
    description: str
    is_active: bool

    class Config:
        orm_mode = True


class CreateItemsSchema(BaseModel):
    """Схема для создания item"""

    name: str
    weight: int
    description: str
    is_active: bool = True

    class Config:
        orm_mode = True


class UpdateItemsSchema(BaseModel):
    """Схема для обновления item"""

    name: str
    weight: int
    description: str
    is_active: bool

    class Config:
        orm_mode = True


# class DeleteItemSchema(BaseModel):
#     """Схема для удаления item"""
#     pass
#
#     class Config:
#         orm_mode = True


# class MyCompound(BaseModel):
#     compound_id: int
#     amount: int
#
#
# class MyCustom(BaseModel):
#     item_id: int
#     compounds: List[MyCompound]






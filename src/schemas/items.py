from pydantic import BaseModel
from typing import List, Optional


class ItemsInfo(BaseModel):
    """Базовая схема для позиций в меню"""

    id: int
    name: str
    weight: int
    description: str
    is_active: bool
    compounds: Optional[List[int]]

    class Config:
        orm_mode = True


class CreateItemsSchema(BaseModel):

    name: str
    weight: int
    description: str
    is_active: bool = True
    compounds: Optional[List[int]] = []

    class Config:
        orm_mode = True


class UpdateItemsSchema(BaseModel):

    id: int
    name: str
    weight: int
    description: str
    is_active: bool
    compounds: Optional[List[str]]

    class Config:
        orm_mode = True



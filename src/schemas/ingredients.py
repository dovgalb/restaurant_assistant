from enum import Enum
from typing import Optional, List

from sqlalchemy import null

from src.db.models import Ingredient as SubIngredients

from pydantic import BaseModel


class IngredientsInfo(BaseModel):
    """Базовая схема для ингредиентов(Лук, Огурцы, Помидор и т.д.)"""

    id: int
    name: str
    parent_id: Optional[int]
    # sub_ingredients: List[int] = []
    # todo придумать как отображать список дочерних ингредиентов

    class Config:
        orm_mode = True


class CreateIngredientSchema(BaseModel):
    """Схема для создания ингредиентов(parent_id используется для привязки одного ингредиента к другому)"""

    name: str
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True


class UpdateIngredientSchema(BaseModel):
    """Схема для обновления ингредиента"""
    name: str
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True

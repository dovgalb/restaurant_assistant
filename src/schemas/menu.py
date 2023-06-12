from datetime import datetime

from pydantic import BaseModel
from typing import Optional, List


class MenuInfo(BaseModel):
    """Базовая схема модели Меню"""

    id: int
    name: str
    description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: bool
    # TODO сделать

    class Config:
        orm_mode = True


class CreateMenuSchema(BaseModel):
    """Базовая схема модели Меню"""

    name: str
    description: Optional[str]
    is_active: bool
    restaurant_ids: Optional[list[int]]
    # created_at: datetime
    # updated_at: datetime


    # TODO сделать

    class Config:
        orm_mode = True


class UpdateMenuSchema(BaseModel):
    """Базовая схема модели Меню"""

    name: str
    description: Optional[str]
    restaurant_ids: Optional[list[int]]
    is_active: bool

    # TODO сделать

    class Config:
        orm_mode = True


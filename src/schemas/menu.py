from datetime import datetime

from pydantic import BaseModel
from typing import Optional, List


class MenuInfo(BaseModel):
    """Базовая схема модели Меню"""

    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
    # TODO сделать

    class Config:
        orm_mode = True


class CreateMenuSchema(BaseModel):
    """Базовая схема модели Меню"""

    id: int
    name: str
    description: Optional[str]
    is_active: bool

    # TODO сделать

    class Config:
        orm_mode = True


class UpdateMenuSchema(BaseModel):
    """Базовая схема модели Меню"""

    id: int

    # TODO сделать

    class Config:
        orm_mode = True

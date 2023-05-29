import enum

from pydantic import BaseModel
from enum import Enum


class SectionEnum(str, Enum):
    BAR = "Bar"
    KITCHEN = "Kitchen"


class CategoriesInfo(BaseModel):
    """Базовая схема для Категории"""

    id: int
    name: str
    section: SectionEnum

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True


class CreateCategorySchema(BaseModel):
    """Базовая схема модели Категории"""

    name: str
    section: SectionEnum

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True


class UpdateCategorySchema(BaseModel):
    """Схема обновления Категории"""

    id: int
    name: str
    section: SectionEnum

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True


class DeleteCategorySchema(BaseModel):
    """Схема для удаления Категории"""

    id: int

    class Config:
        orm_mode = True
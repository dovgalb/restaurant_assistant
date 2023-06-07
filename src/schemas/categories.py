from pydantic import BaseModel


class CategoriesInfo(BaseModel):
    """Базовая схема для Категории"""

    id: int
    name: str
    is_active: bool
    menu_id: int

    class Config:
        orm_mode = True


class CreateCategorySchema(BaseModel):
    """Базовая схема создания Категории"""

    name: str
    is_active: bool
    menu_id: int

    class Config:
        orm_mode = True


class UpdateCategorySchema(BaseModel):
    """Схема обновления Категории"""

    name: str
    is_active: bool
    menu_id: int

    class Config:
        orm_mode = True

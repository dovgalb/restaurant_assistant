from pydantic import BaseModel


class SubcategoriesInfo(BaseModel):
    """Базовая схема для подкатегорий"""

    id: int
    name: str
    category_id: int

    class Config:
        orm_mode = True


class CreateSubcategorySchema(BaseModel):
    """Базовая схема создания подкатегории"""

    name: str
    category_id: int

    class Config:
        orm_mode = True


class UpdateSubcategorySchema(BaseModel):
    """Базовая схема обновления подкатегории"""

    name: str
    category_id: int

    class Config:
        orm_mode = True
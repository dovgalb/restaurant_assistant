from pydantic import BaseModel


class IngredientInfo(BaseModel):
    """Базовая схема для compounds(Лук, Огурцы, Помидор и т.д.)"""

    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True


class CreateIngredientSchema(BaseModel):
    """Схема для создания compounds"""

    name: str
    is_active: bool

    class Config:
        orm_mode = True


class UpdateIngredientSchema(BaseModel):
    """Схема для обновления ингридиента"""
    name: str
    is_active: bool

    class Config:
        orm_mode = True


# class DeleteCompoundSchema(BaseModel):
#
#     class Config:
#         orm_mode = True
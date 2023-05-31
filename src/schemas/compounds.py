from pydantic import BaseModel


class CompoundsInfo(BaseModel):
    """Базовая схема для compounds(Лук, Огурцы, Помидор и т.д.)"""

    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True


class CreateCompoundSchema(BaseModel):
    """Схема для создания compounds"""

    name: str
    is_active: bool

    class Config:
        orm_mode = True


class UpdateCompoundSchema(BaseModel):
    """Схема для обновления ингридиента"""
    name: str
    is_active: bool

    class Config:
        orm_mode = True


# class DeleteCompoundSchema(BaseModel):
#
#     class Config:
#         orm_mode = True
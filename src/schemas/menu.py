from pydantic import BaseModel


class MenuInfo(BaseModel):
    """Базовая схема модели Меню"""

    id: int
    name: str

    # TODO сделать

    class Config:
        orm_mode = True


class CreateMenuSchema(BaseModel):
    """Базовая схема модели Меню"""

    name: str

    # TODO сделать

    class Config:
        orm_mode = True


class UpdateMenuSchema(BaseModel):
    """Базовая схема модели Меню"""

    id: int

    # TODO сделать

    class Config:
        orm_mode = True

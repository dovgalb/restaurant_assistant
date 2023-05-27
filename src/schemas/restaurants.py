from pydantic import BaseModel


class RestaurantsInfo(BaseModel):
    """Базовая схема модели Рестораны"""

    id: int
    name: str

    # TODO сделать

    class Config:
        orm_mode = True


class CreateRestaurantsSchema(BaseModel):
    """Базовая схема модели Рестораны"""

    name: str
    user_id: int

    # TODO сделать

    class Config:
        orm_mode = True


class UpdateRestaurantsSchema(BaseModel):
    """Базовая схема модели Рестораны"""

    id: int

    # TODO сделать

    class Config:
        orm_mode = True

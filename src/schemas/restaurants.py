from pydantic import BaseModel


class RestaurantsList(BaseModel):
    """Базовая схема модели Рестораны"""

    id: int
    #TODO сделать

    class Config:
        orm_mode = True

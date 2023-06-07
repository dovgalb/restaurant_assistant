from src.db.models import Dish
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.dishes import CreateDishSchema, UpdateDishSchema


class DishesRepository(
    SQLAlchemyCRUD[Dish, CreateDishSchema, UpdateDishSchema]
):
    pass


dishes_repository = DishesRepository(Dish)
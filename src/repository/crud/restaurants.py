from src.db.models import Restaurant
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.restaurants import CreateRestaurantsSchema, UpdateRestaurantsSchema


class RestaurantRepository(
    SQLAlchemyCRUD[Restaurant, CreateRestaurantsSchema, UpdateRestaurantsSchema]
):
    pass


restaurant_repository = RestaurantRepository(Restaurant)

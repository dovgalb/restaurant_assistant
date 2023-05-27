from src.db.models import Restaurants
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.restaurants import CreateRestaurantsSchema, UpdateRestaurantsSchema


class RestaurantRepository(
    SQLAlchemyCRUD[Restaurants, CreateRestaurantsSchema, UpdateRestaurantsSchema]
):
    pass


restaurant_repository = RestaurantRepository(Restaurants)

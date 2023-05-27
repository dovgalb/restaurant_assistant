from src.db.models import Restaurants
from src.repository.filter.base import SqlAlchemyFilter


class RestaurantFilter(SqlAlchemyFilter):
    pass


restaurants_filter = RestaurantFilter(Restaurants)

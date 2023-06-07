from src.db.models import Restaurant
from src.repository.filter.base import SqlAlchemyFilter


class RestaurantFilter(SqlAlchemyFilter):
    pass


restaurants_filter = RestaurantFilter(Restaurant)

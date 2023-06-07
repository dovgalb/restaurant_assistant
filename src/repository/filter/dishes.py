from src.db.models import Dish
from src.repository.filter.base import SqlAlchemyFilter


class DishesFilter(SqlAlchemyFilter):
    pass


dishes_filter = DishesFilter(Dish)


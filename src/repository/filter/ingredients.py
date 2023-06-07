from src.db.models import Ingredient
from src.repository.filter.base import SqlAlchemyFilter


class IngredientsFilter(SqlAlchemyFilter):
    pass


ingredients_filter = IngredientsFilter(Ingredient)
from src.db.models import Categories
from src.repository.filter.base import SqlAlchemyFilter


class CategoryFilter(SqlAlchemyFilter):
    pass


category_filter = CategoryFilter(Categories)
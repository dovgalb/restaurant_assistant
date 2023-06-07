from src.db.models import Category
from src.repository.filter.base import SqlAlchemyFilter


class CategoryFilter(SqlAlchemyFilter):
    pass


category_filter = CategoryFilter(Category)

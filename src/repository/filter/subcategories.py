from src.db.models import Subcategory
from src.repository.filter.base import SqlAlchemyFilter


class SubcategoryFilter(SqlAlchemyFilter):
    pass


subcategory_filter = SubcategoryFilter(Subcategory)
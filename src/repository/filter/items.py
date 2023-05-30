from src.db.models import Items
from src.repository.filter.base import SqlAlchemyFilter


class ItemsFilter(SqlAlchemyFilter):
    pass


items_filter = ItemsFilter(Items)


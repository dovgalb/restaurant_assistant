from src.db.models import Menu
from src.repository.filter.base import SqlAlchemyFilter


class MenuFilter(SqlAlchemyFilter):
    pass


menu_filter = MenuFilter(Menu)

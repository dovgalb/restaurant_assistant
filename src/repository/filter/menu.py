from src.db.models import Menus
from src.repository.filter.base import SqlAlchemyFilter


class MenuFilter(SqlAlchemyFilter):
    pass


menu_filter = MenuFilter(Menus)

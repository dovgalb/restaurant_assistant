from src.db.models import Compounds
from src.repository.filter.base import SqlAlchemyFilter


class CompoundsFilter(SqlAlchemyFilter):
    pass


compounds_filter = CompoundsFilter(Compounds)
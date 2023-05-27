"""
Модуль описывает фильтры, ограничивающие выборку сущностей.

Фильтры описывают те условия поиска, которые нужно применить в CRUD
для получения/обновления/создания нужных сущностей.
"""
import copy
from typing import Any, Optional

from sqlalchemy import asc, desc
from sqlalchemy.future import select
from sqlalchemy.sql.elements import BinaryExpression, UnaryExpression
from sqlalchemy.sql.selectable import Select

from src.repository.base import AlchemyModelType


class QueryFilter:
    """Базовый класс фильтра для запроса"""

    def __call__(self):
        return copy.deepcopy(self)

    @property
    def select(self) -> Any:
        """Выражение select для запроса сущностей"""
        return None

    @property
    def where(self) -> Optional[Any]:
        """Устловие для фильтра сущностей"""
        return None

    @property
    def order_by(self) -> Optional[Any]:
        """Сортировка сущностей"""
        return None

    @property
    def limit(self) -> Optional[Any]:
        """Количество возвращаемых сущностей"""
        return None

    @property
    def offset(self) -> Optional[Any]:
        """Смещение, с которого нужно начать искать нужные сущности"""
        return None


class SqlAlchemyFilter(QueryFilter):
    """Фильтры для запросов алхимии"""

    def __init__(self, model: type[AlchemyModelType]):
        super().__init__()

        self._model = model

        self.page: Optional[int] = None
        self.per_page = 25
        self.order: Optional[str] = None

    @property
    def select(self) -> Select:
        """Выражение select для запроса сущностей"""
        return select(self._model)

    @property
    def where(self) -> Optional[BinaryExpression]:
        """Если в фильтр передан id сущности, то фильтруем по нему"""
        return None

    @property
    def order_by(self) -> Optional[UnaryExpression]:
        """Позволяем сортировать записи как в asc, так и в desc порядке"""
        if self.order is None:
            return None

        order_function = asc
        order = self.order
        if order.startswith("-"):
            order = order[1:]  # pylint: disable = unsubscriptable-object
            order_function = desc

        return order_function(order)

    @property
    def limit(self) -> int:
        """limit в основном указвает фронт в запрое"""
        return self.per_page

    @property
    def offset(self) -> Optional[int]:
        """Вычисляем offset для страничной пагинации"""
        if self.page:
            return (self.page - 1) * self.per_page

        return None

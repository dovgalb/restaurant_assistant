from typing import Optional

from sqlalchemy import BinaryExpression, and_

from src.db.models import Restaurant
from fastapi import Query
from src.repository.filter.base import SqlAlchemyFilter


class RestaurantFilter(SqlAlchemyFilter):
    def __call__(
            self,
            restaurant_name: Optional[str] = Query(default=None, example="Публичка"),
    ) -> "RestaurantFilter":

        self.restaurant_name = restaurant_name
        return super().__call__()

    @property
    def where(self) -> Optional[BinaryExpression]:
        """Применение переданных фильтров в блоке WHERE"""
        and_args = []  # type: ignore

        if self.restaurant_name is not None:
            and_args.append(
                self._model.name.icontains(self.restaurant_name)
            )

        return and_(*and_args) if and_args else super().where


restaurants_filter = RestaurantFilter(Restaurant)

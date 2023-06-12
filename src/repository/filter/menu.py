from typing import Optional

from fastapi import Query
from sqlalchemy import BinaryExpression, and_, Select, select

from src.db.models import Menu, Restaurant, RestaurantMenu
from src.repository.filter.base import SqlAlchemyFilter


class MenuFilter(SqlAlchemyFilter):
    def __call__(
            self,
            restaurant_name: Optional[str] = Query(default=None, example="Публичка"),
    ) -> "MenuFilter":
        self.restaurant_name = restaurant_name

        return super().__call__()

    @property
    def select(self) -> Select:
        return select(self._model
                      ).join(RestaurantMenu, RestaurantMenu.menu_id == self._model.id
                             ).join(Restaurant, Restaurant.id == RestaurantMenu.restaurant_id)

    @property
    def where(self) -> Optional[BinaryExpression]:
        """Применение переданных фильтров в блоке WHERE"""
        and_args = []  # type: ignore

        if self.restaurant_name is not None:
            and_args.append(
                Restaurant.name.icontains(self.restaurant_name)
            )

        return and_(*and_args) if and_args else super().where


class MenuFilterEmpty(SqlAlchemyFilter):
    @property
    def select(self) -> Select:
        return select(self._model
                      ).join(RestaurantMenu, RestaurantMenu.menu_id == self._model.id
                             ).join(Restaurant, Restaurant.id == RestaurantMenu.restaurant_id)


menu_filter = MenuFilter(Menu)
menu_filter_empty = MenuFilterEmpty(Menu)
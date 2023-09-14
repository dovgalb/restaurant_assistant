"""Модуль для взаимодействия с БД"""
from typing import Optional

from sqlalchemy import BinaryExpression, UnaryExpression, Select, select

from src.db.models import Menu, Restaurant, RestaurantMenu
from src.repository.base import AlchemyModelType
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.menu import CreateMenuSchema, UpdateMenuSchema


class MenuRepository(
    SQLAlchemyCRUD[Menu, CreateMenuSchema, UpdateMenuSchema]
):
    async def get_menus(
            self,
            restaurant_id: int,
            select_statement: Optional[Select] = None,
            where_expression: Optional[BinaryExpression] = None,
            order_by: Optional[UnaryExpression] = None,
            limit: Optional[int] = None,
            offset: Optional[int] = None,
    ) -> list[AlchemyModelType]:
        """Возвращает список объектов по переданным фильтрам"""
        select_st = select(self._model)
        if select_statement is not None:
            select_st = select_statement

        if where_expression is not None:
            select_st = select_st.where(where_expression)

        if order_by is not None:
            select_st = select_st.order_by(order_by)

        if offset is not None:
            select_st = select_st.offset(offset)

        if limit is not None:
            select_st = select_st.limit(limit)

        select_st = select_st.where(Restaurant.id == restaurant_id)
        res = await self.db_session.execute(select_st)  # type: ignore
        return res.scalars().all()

    async def create(self, obj_in: dict) -> AlchemyModelType:

        menu = self._model(**obj_in)
        self.db_session.add(menu)  # type: ignore
        return menu

    async def create_restaurant_menu(self, menu_id: int, restaurant_ids: Optional[list[int]]):
        restaurant_menus: list = []
        for restaurant_id in restaurant_ids:
            restaurant_menus.append(RestaurantMenu(restaurant_id=restaurant_id, menu_id=menu_id))
        self.db_session.add_all(restaurant_menus)  # type: ignore


menu_repository = MenuRepository(Menu)

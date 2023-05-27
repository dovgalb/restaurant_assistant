"""Модуль для взаимодействия с БД"""
from src.db.models import Menus
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.menu import CreateMenuSchema, UpdateMenuSchema


class MenuRepository(
    SQLAlchemyCRUD[Menus, CreateMenuSchema, UpdateMenuSchema]
):
    pass


menu_repository = MenuRepository(Menus)

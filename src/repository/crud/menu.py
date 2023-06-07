"""Модуль для взаимодействия с БД"""
from src.db.models import Menu
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.menu import CreateMenuSchema, UpdateMenuSchema


class MenuRepository(
    SQLAlchemyCRUD[Menu, CreateMenuSchema, UpdateMenuSchema]
):
    pass


menu_repository = MenuRepository(Menu)

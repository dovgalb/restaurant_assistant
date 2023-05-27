"""Модуль для бизнес-логики"""
from repository.crud.menu import menu_repository
from repository.unit_of_work.base import SqlAlchemyUnitOfWork
from schemas.menu import MenuInfo
from services.base import CrudService


class MenuService(CrudService):
    pass


def menu_service() -> MenuService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=menu_repository,
    )

    return MenuService(
        unit_of_work=unit_of_work,
        read_schema=MenuInfo,
    )
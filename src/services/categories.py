"""Модуль для бизнес-логики"""
from src.repository.crud.categories import category_repository
from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.schemas.categories import CategoriesInfo

class CategoriesService(CrudService):
    pass


def category_service() -> CategoriesService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=category_repository,
    )

    return CategoriesService(
        unit_of_work=unit_of_work,
        read_schema=CategoriesInfo,
    )
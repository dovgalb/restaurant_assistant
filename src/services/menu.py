"""Модуль для бизнес-логики"""
from repository.base import ReadSchemaType, CreateSchemaType
from repository.filter.base import QueryFilter
from src.repository.crud.menu import menu_repository
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.schemas.menu import MenuInfo
from src.services.base import CrudService


class MenuService(CrudService):
    async def get_menus(
            self,
            restaurant_id: int,
            query_filter: QueryFilter,
    ) -> list[ReadSchemaType]:
        """Получаем список сущностей по переданным фильтрам"""
        async with self._uow as uow:
            entities = await uow.repository.get_menus(
                restaurant_id,
                query_filter.select,
                query_filter.where,
                query_filter.order_by,
                query_filter.limit,
                query_filter.offset,
            )

        return [self._serialize(entity) for entity in entities]

    async def _create(self, data: CreateSchemaType) -> ReadSchemaType:
        """Создаем новую сущность и при необходимости кэшируем"""
        menu_data = data.dict()
        restaurant_ids = menu_data.pop("restaurant_ids")
        async with self._uow as uow:
            entity = await uow.repository.create(menu_data)

        async with self._uow as uow:
            await uow.repository.create_restaurant_menu(entity.id, restaurant_ids)

        entity = self._serialize(entity)

        return entity


def menu_service() -> MenuService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=menu_repository,
    )

    return MenuService(
        unit_of_work=unit_of_work,
        read_schema=MenuInfo,
    )
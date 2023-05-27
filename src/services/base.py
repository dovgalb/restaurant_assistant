"""
Сервис - модуль, в котором бизнес-логика встречается
с инфраструктурным кодом (базами данных, кэшами, брокерами и тд).

Данный модуль реализует стандартный сервис, позволяющий
выполнять обычные CRUD операции.
"""

from typing import Any

from src.db.base import Base
from src.repository.base import ReadSchemaType, CreateSchemaType, UpdateSchemaType
from src.repository.filter.base import QueryFilter
from src.repository.unit_of_work.base import UnitOfWork


class CrudService:
    """
    Класс реализует стандартный сервис, позволяющий
    выполнять обычные CRUD операции.
    """

    def __init__(
            self,
            unit_of_work: UnitOfWork,
            read_schema: type[ReadSchemaType],
    ):
        self._uow = unit_of_work
        self._read_schema = read_schema

    def _serialize(self, entity: Any) -> ReadSchemaType:
        """Сериализуем сущность после ее создания/получения/бновления"""
        if isinstance(entity, Base):
            return self._read_schema.from_orm(entity)

        return self._read_schema(**entity)

    async def _create(self, data: CreateSchemaType) -> ReadSchemaType:
        """Создаем новую сущность и при необходимости кэшируем"""
        async with self._uow as uow:
            entity = await uow.repository.create(data)

        entity = self._serialize(entity)

        return entity

    async def _bulk_create(self, data: list[CreateSchemaType]) -> None:
        """Создаем новую сущность из списка обьектов"""
        async with self._uow as uow:
            await uow.repository.bulk_create(data)
        return None

    async def _retrieve(self, entity_id: int) -> ReadSchemaType:
        """Получаем сущность по ее id"""

        async with self._uow as uow:
            if not (entity := await uow.repository.get_by_id(entity_id)):
                return entity  # type: ignore

        entity = self._serialize(entity)

        return entity

    async def _list(self, query_filter: QueryFilter) -> list[ReadSchemaType]:
        """Получаем список сущностей по переданным фильтрам"""
        async with self._uow as uow:
            entities = await uow.repository.get_multi(
                query_filter.select,
                query_filter.where,
                query_filter.order_by,
                query_filter.limit,
                query_filter.offset,
            )

        return [self._serialize(entity) for entity in entities]

    async def _update(
            self,
            entity_id: int,
            data: UpdateSchemaType,
    ) -> ReadSchemaType:
        """
        Обновляем сущность, взятую по id.
        При неоходимости кэшируем ее.
        """
        async with self._uow as uow:
            entity = await uow.repository.update_by_id(entity_id, data)

        if entity:
            entity = self._serialize(entity)

        return entity

    async def _delete(self, entity_id: int):
        """Удаляем сущность по id"""
        async with self._uow as uow:
            await uow.repository.remove_by_id(entity_id)

    async def _count(self, list_filter: QueryFilter) -> int:
        """Считаем число сущностей по переданным фильтрам"""
        async with self._uow as uow:
            count = await uow.repository.count(
                list_filter.select, list_filter.where
            )

        return count

    async def _list_extremist_materials(self) -> list[ReadSchemaType]:
        """Получаем список сущностей по переданным фильтрам"""
        async with self._uow as uow:
            entities = await uow.repository.get_multi()

        return [self._serialize(entity) for entity in entities]

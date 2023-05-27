from typing import Any, Optional, Union, Generic

from sqlalchemy import Select, BinaryExpression, select, func, UnaryExpression, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.configs import get_settings
from src.repository.base import ModelType, CreateSchemaType, UpdateSchemaType, AlchemyModelType
from src.repository.crud.exception import check_session

settings = get_settings()


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Базовый класс по созданию/чтению/обновлению/удалению сущностей"""

    async def get(self, where_expression: Any) -> Optional[ModelType]:
        """Получаем сущность по условию"""
        raise NotImplementedError

    async def get_multi(
        self,
        select_statement: Any = None,
        where_expression: Any = None,
        order_by: Any = None,
        limit: Any = None,
        offset: Any = None,
    ) -> list[ModelType]:
        """Получаем список сущностей по условию"""
        raise NotImplementedError

    async def get_by_id(self, entity_id: Any) -> Optional[ModelType]:
        """Получаем список сущностей по id"""
        raise NotImplementedError

    async def count(
        self, select_statement: Any = None, where_expression: Any = None
    ) -> int:
        """Считаем количество сущностей по условию"""
        raise NotImplementedError

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Создаем сущность"""
        raise NotImplementedError

    async def bulk_create(
        self,
        objects_in: list[CreateSchemaType],
    ) -> list[ModelType]:
        """Массово создаем сущности"""
        raise NotImplementedError

    async def update(
        self,
        obj_data: Union[UpdateSchemaType, dict[str, Any]],
        where_expression: Any,
    ) -> Optional[ModelType]:
        """Обновляем сущности по условию"""
        raise NotImplementedError

    async def update_by_id(
        self,
        obj_id: Any,
        obj_data: Union[UpdateSchemaType, dict[str, Any]],
    ) -> Optional[ModelType]:
        """Обновляем сущность по id"""
        raise NotImplementedError

    async def remove(self, where_expression: Any) -> None:
        """Удаляем сущности по условию"""
        raise NotImplementedError

    async def remove_by_id(self, entity_id: Any) -> None:
        """Удаляем сущность по id"""
        raise NotImplementedError


class SQLAlchemyCRUD(CRUDBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Класс по созданию/чтению/обновлению/удалению сущностей
    с использоваием методов ром sqlalchemy
    """

    def __init__(self, model: type[AlchemyModelType]):
        self._model = model
        self.db_session: Optional[AsyncSession] = None

    def __call__(self, db_session: AsyncSession) -> "SQLAlchemyCRUD":
        self.db_session = db_session
        return self

    @check_session
    async def get(
        self, where_expression: BinaryExpression
    ) -> Optional[AlchemyModelType]:
        """Возвращает объект по переданным фильтрам"""
        res = await self.db_session.execute(  # type: ignore
            select(self._model).where(where_expression)
        )
        return res.scalars().one_or_none()

    @check_session
    async def get_multi(
        self,
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

        res = await self.db_session.execute(select_st)  # type: ignore
        return res.scalars().all()

    @check_session
    async def get_by_id(self, entity_id: Any) -> Optional[AlchemyModelType]:
        """Возвращает из БД объект по его id"""
        return await self.get(self._model.id == entity_id)

    @check_session
    async def count(
        self,
        select_statement: Optional[Select] = None,
        where_expression: Optional[BinaryExpression] = None,
    ) -> int:
        """Считает количество объектов по переданным фильтрам"""
        select_st = select(self._model)
        if select_statement is not None:
            select_st = select_statement

        if where_expression is not None:
            select_st = select_st.where(where_expression)

        res = await self.db_session.execute(  # type: ignore
            select(func.count()).select_from(select_st)
        )
        return res.scalar_one()

    @check_session
    async def create(self, obj_in: CreateSchemaType) -> AlchemyModelType:
        """Делает запись объекта в БД"""
        db_obj = self._model(**obj_in.dict())
        self.db_session.add(db_obj)  # type: ignore
        return db_obj

    @check_session
    async def bulk_create(
        self,
        objects_in: list[CreateSchemaType],
    ) -> list[AlchemyModelType]:
        """Создает в бд множество сущностей за один запрос"""
        return await self.db_session.execute(  # type: ignore
            insert(self._model).returning(self._model),
            [obj.dict() for obj in objects_in],
        )

    @check_session
    async def update(
        self,
        obj_data: Union[UpdateSchemaType, dict[str, Any]],
        where_expression: BinaryExpression,
    ) -> Optional[AlchemyModelType]:
        """Обновляет объект в бд по заданному условию where"""
        if not isinstance(obj_data, dict):
            obj_data = obj_data.dict()

        update_st = (
            update(self._model).where(where_expression).values(**obj_data)
        )

        await self.db_session.execute(update_st)  # type: ignore
        return await self.get(where_expression)

    @check_session
    async def update_by_id(
        self, obj_id: Any, obj_data: Union[UpdateSchemaType, dict[str, Any]]
    ) -> Optional[AlchemyModelType]:
        """Обновляет объект в бд по id"""
        return await self.update(obj_data, self._model.id == obj_id)

    @check_session
    async def remove(self, where_expression: BinaryExpression) -> None:
        """Удаляет объект из бд по заданному условию where"""
        await self.db_session.execute(  # type: ignore
            delete(self._model).where(where_expression)
        )

    @check_session
    async def remove_by_id(self, entity_id: Any):
        """Удаляет объект из бд по id"""
        await self.remove(self._model.id == entity_id)
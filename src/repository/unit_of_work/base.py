"""
Репозиторий (модуь crud)
позволяет изолировать логику работы с БД и написания запросов,

Однако для работы репозитория нужно передавать ему сессию бд.
Шаблон Unit of Work позволяет изолировать работу с сессиями БД,
а также упростить работу с различными репозиториями.
"""

from collections.abc import Callable

from sqlalchemy.exc import IntegrityError

from src.db.session import db_session_maker
from src.repository.crud.base import CRUDBase, SQLAlchemyCRUD


class UnitOfWork:
    """Реализует шаблон UoW"""

    repository: CRUDBase

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, *args):
        await self.rollback()

    async def begin(self):
        """Транзакция"""
        raise NotImplementedError

    async def commit(self):
        """Применить изменения"""
        raise NotImplementedError

    async def rollback(self):
        """Откатить изменения"""
        raise NotImplementedError


class SqlAlchemyUnitOfWork(UnitOfWork):
    """
    Реализует шаблон UoW и управляет сессиями БД
    """

    repository: SQLAlchemyCRUD

    def __init__(
            self,
            repository: SQLAlchemyCRUD,
            session_maker: Callable = db_session_maker,
    ):
        self.session_maker = session_maker
        self.repository = repository

        self.db_session = None

    async def __aenter__(self) -> "SqlAlchemyUnitOfWork":
        self.db_session = self.session_maker()
        self.repository = self.repository(self.db_session)
        return self

    async def __aexit__(self, *args):
        await self.commit()
        await self.db_session.close()

    async def begin(self):
        """Транзакция бд"""
        async with self.db_session.begin():
            yield

    async def commit(self):
        """Применяем изменения в бд"""
        try:
            await self.db_session.commit()
        except IntegrityError as error:
            await self.rollback()
            raise error

    async def rollback(self):
        """Откатываем изменения в бд"""
        await self.db_session.rollback()

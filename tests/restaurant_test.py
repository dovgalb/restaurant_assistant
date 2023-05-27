import asyncio
from typing import Callable

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from main import app
from src.db.base import Base
from src.repository.crud.base import SQLAlchemyCRUD
from src.repository.crud.restaurants import restaurant_repository
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.schemas.restaurants import RestaurantsInfo, CreateRestaurantsSchema
from src.services.restaurants import RestaurantService, restaurant_service

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


class TestSqlAlchemyUnitOfWork(SqlAlchemyUnitOfWork):
    def __init__(
            self,
            repository: SQLAlchemyCRUD,
            session_maker: Callable = sessionmaker(engine, future=True, expire_on_commit=False, class_=AsyncSession),
    ):
        super().__init__(repository, session_maker)


def fake_restaurant_service():
    uow = TestSqlAlchemyUnitOfWork(repository=restaurant_repository)
    return RestaurantService(
        unit_of_work=uow,
        read_schema=RestaurantsInfo,
    )


@pytest.fixture(scope="session")
def wipe_db():
    async def drop_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(drop_tables())
    yield

    asyncio.run(drop_tables())


@pytest.fixture(scope="function")
def client():
    app.dependency_overrides[restaurant_service] = fake_restaurant_service

    return TestClient(app)


def test_create_restaurant(wipe_db, client):
    restaurant = CreateRestaurantsSchema(name="chimichangas4life", user_id=1)
    response = client.post(
        "/restaurants/",
        json=restaurant.dict(),
    )
    assert response.status_code == 200
    data = response.json()
    assert restaurant.name == data["name"]

from src.schemas.dishes import DishesInfo
from src.repository.crud.dishes import dishes_repository
from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork


class DishesService(CrudService):
    pass


def dishes_service() -> DishesService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=dishes_repository
    )

    return DishesService(
        unit_of_work=unit_of_work,
        read_schema=DishesInfo,
    )
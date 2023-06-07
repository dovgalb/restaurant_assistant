from src.repository.crud.restaurants import restaurant_repository
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.schemas.restaurants import RestaurantsInfo
from src.services.base import CrudService


class RestaurantService(CrudService):
    pass


def restaurant_service() -> RestaurantService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=restaurant_repository,
    )

    return RestaurantService(
        unit_of_work=unit_of_work,
        read_schema=RestaurantsInfo,
    )

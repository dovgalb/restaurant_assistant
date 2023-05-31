from schemas.items import ItemsInfo
from src.repository.crud.items import items_repository
from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork


class ItemsService(CrudService):
    pass


def items_service() -> ItemsService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=items_repository
    )

    return ItemsService(
        unit_of_work=unit_of_work,
        read_schema=ItemsInfo,
    )
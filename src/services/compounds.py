from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.repository.crud.compounds import compounds_repository
from src.schemas.compounds import CompoundsInfo


class CompoundsService(CrudService):
    pass


def compounds_service() -> CompoundsService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=compounds_repository
    )

    return CompoundsService(
        unit_of_work=unit_of_work,
        read_schema=CompoundsInfo,
    )
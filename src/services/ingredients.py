from src.services.base import CrudService
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork
from src.repository.crud.ingredients import ingredients_repository
from src.schemas.ingredients import IngredientsInfo


class IngredientService(CrudService):
    pass


def ingredient_service() -> IngredientService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=ingredients_repository
    )

    return IngredientService(
        unit_of_work=unit_of_work,
        read_schema=IngredientsInfo,
    )
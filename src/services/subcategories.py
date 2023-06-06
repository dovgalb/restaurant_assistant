from src.schemas.subcategories import SubcategoriesInfo
from src.services.base import CrudService
from src.repository.crud.subcategories import subcategories_repository
from src.repository.unit_of_work.base import SqlAlchemyUnitOfWork

class SubcategoryService(CrudService):
    pass


def subcategory_service() -> SubcategoryService:
    unit_of_work = SqlAlchemyUnitOfWork(
        repository=subcategories_repository
    )

    return SubcategoryService(
        unit_of_work=unit_of_work,
        read_schema=SubcategoriesInfo
    )
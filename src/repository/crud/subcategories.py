from src.db.models import Subcategory
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.subcategories import CreateSubcategorySchema, UpdateSubcategorySchema


class SubcategoryRepository(
    SQLAlchemyCRUD[Subcategory, CreateSubcategorySchema, UpdateSubcategorySchema]
):
    pass


subcategories_repository = SubcategoryRepository(Subcategory)

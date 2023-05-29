from src.db.models import Categories
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.categories import CreateCategorySchema, UpdateCategorySchema


class CategoryRepository(
    SQLAlchemyCRUD[Categories, CreateCategorySchema, UpdateCategorySchema]
):
    pass


category_repository = CategoryRepository(Categories)
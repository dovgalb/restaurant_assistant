from src.db.models import Category
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.categories import CreateCategorySchema, UpdateCategorySchema


class CategoryRepository(
    SQLAlchemyCRUD[Category, CreateCategorySchema, UpdateCategorySchema]
):
    pass


category_repository = CategoryRepository(Category)
from src.db.models import Ingredient
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.ingredients import CreateIngredientSchema, UpdateIngredientSchema


class CompoundsRepository(
    SQLAlchemyCRUD[Ingredient, CreateIngredientSchema, UpdateIngredientSchema]
):
    pass


compounds_repository = CompoundsRepository(Ingredient)
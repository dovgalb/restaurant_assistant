from src.db.models import Ingredient
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.ingredients import CreateIngredientSchema, UpdateIngredientSchema


class IngredientRepository(
    SQLAlchemyCRUD[Ingredient, CreateIngredientSchema, UpdateIngredientSchema]
):
    pass


ingredients_repository = IngredientRepository(Ingredient)
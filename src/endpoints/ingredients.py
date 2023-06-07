from fastapi import APIRouter, Depends
from typing import List

from src.services.ingredients import ingredient_service
from src.schemas.ingredients import IngredientsInfo, CreateIngredientSchema, UpdateIngredientSchema
from src.repository.filter.ingredients import ingredients_filter

ingredients_router = APIRouter()


@ingredients_router.get("/", response_model=List[IngredientsInfo])
async def get_compounds(
        service=Depends(ingredient_service)
):
    return await service._list(ingredients_filter)


@ingredients_router.post("/", response_model=CreateIngredientSchema)
async def create_compound(
        data: CreateIngredientSchema,
        service=Depends(ingredient_service)
):
    """Создает ингредиент"""
    return await service._create(data)


@ingredients_router.put("/{ingredient_id}", response_model=UpdateIngredientSchema)
async def update_compound(
        ingredient_id: int,
        data: UpdateIngredientSchema,
        service=Depends(ingredient_service)
):
    """Обновляет ингредиент"""
    return await service._update(data=data, entity_id=ingredient_id)


@ingredients_router.delete("/{ingredient_id}")
async def delete_compound(
        ingredient_id: int,
        service=Depends(ingredient_service)
):
    """Удаляет ингредиент"""
    return await service._delete(entity_id=ingredient_id)





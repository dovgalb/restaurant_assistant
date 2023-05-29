from typing import List
from fastapi import APIRouter, Depends

from src.schemas.categories import CategoriesInfo, CreateCategorySchema
from src.services.categories import category_service
from src.repository.filter.categories import category_filter
category_router = APIRouter()


@category_router.get('/', response_model=List[CategoriesInfo])
async def get_categories(
        service=Depends(category_service)
):
    """Получение списка категорий"""
    return await service._list(category_filter)


@category_router.post('/', response_model=CreateCategorySchema)
async def create_category(
        data: CreateCategorySchema,
        service=Depends(category_service)
):
    return await service._create(data)
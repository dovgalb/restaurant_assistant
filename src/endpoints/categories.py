from typing import List
from fastapi import APIRouter, Depends

from src.schemas.categories import CategoriesInfo, CreateCategorySchema, UpdateCategorySchema
from src.services.categories import category_service
from src.repository.filter.categories import category_filter

category_router = APIRouter()


@category_router.get('/', response_model=List[CategoriesInfo])
async def get_categories(
        service=Depends(category_service)
):
    """Получение списка категорий(салаты, десерты, коктейли)"""
    return await service._list(category_filter)


@category_router.post('/', response_model=CreateCategorySchema)
async def create_category(
        data: CreateCategorySchema,
        service=Depends(category_service)
):
    """Создание категории(section возможно только 'бар' или 'кухня')"""
    return await service._create(data)


@category_router.put('/{category_id}', response_model=UpdateCategorySchema)
async def update_category(
        category_id: int,
        data: UpdateCategorySchema,
        service=Depends(category_service)
):
    """Создание категории(section возможно только 'бар' или 'кухня')"""
    return await service._update(data=data, entity_id=category_id)


@category_router.delete('/{category_id}')
async def delete_category(
        category_id: int,
        service=Depends(category_service)
):
    """Удаление категории"""
    return await service._delete(entity_id=category_id)
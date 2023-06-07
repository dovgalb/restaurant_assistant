from typing import List

from fastapi import APIRouter, Depends
from src.schemas.subcategories import SubcategoriesInfo, CreateSubcategorySchema, UpdateSubcategorySchema
from src.services.subcategories import subcategory_service
from src.repository.filter.subcategories import subcategory_filter
subcategory_router = APIRouter()


@subcategory_router.get('/', response_model=List[SubcategoriesInfo])
async def get_subcategories(
        service=Depends(subcategory_service)
):
    """Получение списка подкатегорий"""
    return await service._list(subcategory_filter)


@subcategory_router.post('/', response_model=CreateSubcategorySchema)
async def create_subcategory(
        data: CreateSubcategorySchema,
        service=Depends(subcategory_service)
):
    """Создание подкатегории(Основные блюда, коктейли, гарниры, и т.д.)"""
    return await service._create(data=data)


@subcategory_router.put('/{subcategory_id}/', response_model=UpdateSubcategorySchema)
async def update_subcategory(
        subcategory_id: int,
        data: UpdateSubcategorySchema,
        service=Depends(subcategory_service)
):
    """Обновление подкатегории"""
    return await service._update(data=data, entity_id=subcategory_id)


@subcategory_router.delete('/{subcategory_id}')
async def delete_subcategory(
        subcategory_id: int,
        service=Depends(subcategory_service)
):
    """Удаление подкатегории"""
    return await service._delete(entity_id=subcategory_id)
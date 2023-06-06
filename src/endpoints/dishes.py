"""
Модуль эндпоинтов для сущности Items(позиции в меню)
"""
from typing import List
from fastapi import APIRouter, Depends

from src.schemas.dishes import ItemsInfo, CreateItemsSchema, UpdateItemsSchema
from src.services.dishes import items_service
from src.repository.filter.dishes import items_filter

item_router = APIRouter()


@item_router.get('/', response_model=List[ItemsInfo])
async def get_items(service=Depends(items_service)):
    """Получение списка items"""
    return await service._list(items_filter)


@item_router.post('/', response_model=CreateItemsSchema)
async def create_item(
        data: CreateItemsSchema,
        service=Depends(items_service)
):
    """Создает item"""
    return await service._create(data)


@item_router.put('/{item_id}/', response_model=UpdateItemsSchema)
async def update_item(
        item_id: int,
        data: CreateItemsSchema,
        service=Depends(items_service)
):
    """Обновление item"""
    return await service._update(data=data, entity_id=item_id)


@item_router.delete("/{item_id}")
async def delete_item(
        item_id: int,
        service=Depends(items_service)
):
    """Удаление item"""
    return await service._delete(entity_id=item_id)

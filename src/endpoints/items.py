"""
Модуль эндпоинтов для сущности Items(позиции в меню)
"""
from typing import List
from fastapi import APIRouter, Depends

from src.schemas.items import ItemsInfo, CreateItemsSchema
from src.services.items import items_service
from src.repository.filter.items import items_filter

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
"""
Модуль эндпоинтов для сущности Items(позиции в меню)
"""
from typing import List
from fastapi import APIRouter, Depends

from src.schemas.dishes import DishesInfo, CreateDishSchema, UpdateDishSchema
from src.services.dishes import dishes_service
from src.repository.filter.dishes import dishes_filter

dish_router = APIRouter()


@dish_router.get('/', response_model=List[DishesInfo])
async def get_items(service=Depends(dishes_service)):
    """Получение списка блюд"""
    return await service._list(dishes_filter)


@dish_router.post('/', response_model=CreateDishSchema)
async def create_item(
        data: CreateDishSchema,
        service=Depends(dishes_service)
):
    """Создает блюда"""
    return await service._create(data)


@dish_router.put('/{dish_id}/', response_model=UpdateDishSchema)
async def update_item(
        dish_id: int,
        data: UpdateDishSchema,
        service=Depends(dishes_service)
):
    """Обновление блюда"""
    return await service._update(data=data, entity_id=dish_id)


@dish_router.delete("/{dish_id}")
async def delete_item(
        dish_id: int,
        service=Depends(dishes_service)
):
    """Удаление блюда"""
    return await service._delete(entity_id=dish_id)

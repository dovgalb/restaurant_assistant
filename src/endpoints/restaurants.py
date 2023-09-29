"""
Модуль для эндпоинтов сущности Рестораны
"""
from typing import List

from fastapi import APIRouter, Depends

from src.repository.filter.restaurants import restaurants_filter, RestaurantFilter
from src.schemas.restaurants import RestaurantsInfo, CreateRestaurantsSchema, UpdateRestaurantsSchema
from src.services.restaurants import restaurant_service

restaurant_router = APIRouter()


@restaurant_router.get("/", response_model=List[RestaurantsInfo])
async def get_restaurants(
        search: RestaurantFilter = Depends(restaurants_filter),
        service=Depends(restaurant_service)
):
    """Получение списка всех ресторанов."""
    return await service._list(search)


@restaurant_router.post("/", response_model=CreateRestaurantsSchema)
async def create_restaurant(
    data: CreateRestaurantsSchema,
    # user: Depends(get_user),
    service=Depends(restaurant_service)
):
    """Создание ресторана"""
    return await service._create(data)


@restaurant_router.put('/{restaurant_id}', response_model=UpdateRestaurantsSchema)
async def update_restaurant(
        restaurant_id: int,
        data: UpdateRestaurantsSchema,
        service=Depends(restaurant_service)
):
    """Обновление данных ресторана"""
    return await service._update(data=data, entity_id=restaurant_id)


@restaurant_router.delete('/{restaurant_id}')
async def delete_restaurant(
        restaurant_id: int,
        service=Depends(restaurant_service)
):
    """Удаление ресторана по id"""
    return await service._delete(entity_id=restaurant_id)

"""
Модуль для эндпоинтов сущности Рестораны
"""
from typing import List

from fastapi import APIRouter, Depends

from src.repository.filter.restaurants import restaurants_filter
from src.schemas.restaurants import RestaurantsInfo, CreateRestaurantsSchema
from src.services.restaurants import restaurant_service

restaurant_router = APIRouter()


@restaurant_router.get("/", response_model=List[RestaurantsInfo])
async def get_restaurants(service=Depends(restaurant_service)):
    """Получение списка ресторанов"""
    return await service._list(restaurants_filter)


@restaurant_router.post("/", response_model=RestaurantsInfo)
async def create_restaurant(
    data: CreateRestaurantsSchema,
    service=Depends(restaurant_service)
):
    """Получение списка ресторанов"""
    return await service._create(data)

"""
Модуль для эндпоинтов сущности Рестораны
"""
from typing import List

from fastapi import APIRouter

from src.repository.filter.restaurants import restaurants_filter
from src.schemas.restaurants import RestaurantsList, CreateRestaurantsSchema
from src.services.restaurants import restaurant_service

restaurant_router = APIRouter()


@restaurant_router.get("/", response_model=List[RestaurantsList])
async def get_restaurants():
    """Получение списка ресторанов"""
    service = restaurant_service()
    return await service._list(restaurants_filter)


@restaurant_router.post("/", response_model=RestaurantsList)
async def create_restaurant(
    data: CreateRestaurantsSchema,
):
    """Получение списка ресторанов"""
    service = restaurant_service()
    return await service._create(data)

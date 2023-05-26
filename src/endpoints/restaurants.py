"""
Модуль для эндпоинтов сущности Рестораны
"""
from fastapi import APIRouter

from src.schemas.restaurants import RestaurantsList
from src.services.restaurants import restaurant_service

restaurant_router = APIRouter()


@restaurant_router.get("/", response_model=RestaurantsList)
async def get_restaurants():
    """Получение списка ресторанов"""
    service = restaurant_service()
    return await service.list()

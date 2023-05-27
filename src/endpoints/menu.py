"""
Модуль для эндпоинтов сущности Меню
"""
from typing import List
from fastapi import APIRouter, Depends
from repository.filter.menu import menu_filter
from schemas.menu import MenuInfo
from services.menu import menu_service

menu_router = APIRouter()


@menu_router.get("/", response_model=List[MenuInfo])
async def get_menus(service=Depends(menu_service)):
    """Получение списка меню"""
    return await service._list(menu_filter)

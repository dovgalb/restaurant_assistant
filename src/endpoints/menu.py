"""
Модуль для эндпоинтов сущности Меню
"""
from typing import List
from fastapi import APIRouter, Depends

from src.repository.filter.menu import menu_filter
from src.schemas.menu import MenuInfo, CreateMenuSchema, UpdateMenuSchema, DeleteMenuSchema
from src.services.menu import menu_service

menu_router = APIRouter()


@menu_router.get("/", response_model=List[MenuInfo])
async def get_menus(service=Depends(menu_service)):
    """Получение списка меню"""
    return await service._list(menu_filter)


@menu_router.post('/', response_model=CreateMenuSchema)
async def create_menu(
        data: CreateMenuSchema,
        service=Depends(menu_service)
):
    """Создание экземпляра меню"""
    return await service._create(data)


@menu_router.put('/', response_model=UpdateMenuSchema)
async def update_menu(
        data: UpdateMenuSchema,
        service=Depends(menu_service)
):
    """Обновление экземпляра меню"""
    return await service._update(data=data, entity_id=data.id)


@menu_router.delete('/')
async def delete_menu(
        data: DeleteMenuSchema,
        service=Depends(menu_service)
):
    """Удаляет меню"""
    return await service._delete(entity_id=data.id)
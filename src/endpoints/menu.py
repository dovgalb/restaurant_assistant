"""
Модуль для эндпоинтов сущности Меню
"""
from typing import List
from fastapi import APIRouter, Depends

from src.repository.filter.menu import menu_filter, MenuFilter, MenuFilterEmpty, menu_filter_empty
from src.schemas.menu import MenuInfo, CreateMenuSchema, UpdateMenuSchema
from src.services.menu import menu_service

menu_router = APIRouter()


@menu_router.get("/menus", response_model=List[MenuInfo])
async def get_menus_for_admin(
        query_filter: MenuFilter = Depends(menu_filter),
        service=Depends(menu_service)):
    """Получение списка меню"""
    return await service._list(query_filter)


@menu_router.get("/{restaurant_id}/menus/", response_model=List[MenuInfo])
async def get_menus(
        restaurant_id: int,
        service=Depends(menu_service)):
    """Получение списка меню для ресторана"""
    return await service.get_menus(restaurant_id, menu_filter_empty)


@menu_router.post('/menus', response_model=CreateMenuSchema)
async def create_menu(
        data: CreateMenuSchema,
        service=Depends(menu_service)
):
    """Создание экземпляра меню"""
    return await service._create(data)


@menu_router.put('/menus/{menu_id}', response_model=UpdateMenuSchema)
async def update_menu(
        menu_id: int,
        data: UpdateMenuSchema,
        service=Depends(menu_service)
):
    """Обновление экземпляра меню"""
    return await service._update(data=data, entity_id=menu_id)


@menu_router.delete('/menus/{menu_id}')
async def delete_menu(
        menu_id: int,
        service=Depends(menu_service)
):
    """Удаляет меню"""
    return await service._delete(entity_id=menu_id)
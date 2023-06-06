from fastapi import APIRouter, Depends
from typing import List

from src.services.compounds import compounds_service
from src.schemas.ingredients import CompoundsInfo, CreateCompoundSchema, UpdateCompoundSchema
from src.repository.filter.compounds import compounds_filter

compounds_router = APIRouter()


@compounds_router.get("/", response_model=List[CompoundsInfo])
async def get_compounds(
        service=Depends(compounds_service)
):
    return await service._list(compounds_filter)


@compounds_router.post("/", response_model=CreateCompoundSchema)
async def create_compound(
        data: CreateCompoundSchema,
        service=Depends(compounds_service)
):
    """Создает ингредиент"""
    return await service._create(data)


@compounds_router.put("/{compound_id}", response_model=UpdateCompoundSchema)
async def update_compound(
        compound_id: int,
        data: UpdateCompoundSchema,
        service=Depends(compounds_service)
):
    """Обновляет ингредиент"""
    return await service._update(data=data, entity_id=compound_id)


@compounds_router.delete("/{compound_id}")
async def delete_compound(
        compound_id: int,
        service=Depends(compounds_service)
):
    """Удаляет ингредиент"""
    return await service._delete(entity_id=compound_id)





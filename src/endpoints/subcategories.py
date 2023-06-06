from typing import List

from fastapi import APIRouter, Depends
from src.schemas.subcategories import SubcategoriesInfo, CreateSubcategorySchema, UpdateSubcategorySchema
from src.services.subcategories import subcategory_service

subcategory_router = APIRouter()

@subcategory_router.get('/', response_model=List[SubcategoriesInfo])
async def get_subcategories(
        service=Depends(subcategory_service)
):
    return await service._list(subcategory_filter)
from src.db.models import Items
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.items import CreateItemsSchema, UpdateItemsSchema


class ItemsRepository(
    SQLAlchemyCRUD[Items, CreateItemsSchema, UpdateItemsSchema]
):
    pass


items_repository = ItemsRepository(Items)
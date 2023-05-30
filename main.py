from fastapi import FastAPI

from src.endpoints.categories import category_router
from src.endpoints.menu import menu_router
from src.endpoints.restaurants import restaurant_router
from src.endpoints.items import item_router

app = FastAPI(
    title="Restaurant Assistant"
)

app.include_router(restaurant_router, prefix="/restaurants",  tags=["Restaurants"],)
app.include_router(menu_router, prefix="/menu", tags=["Menu"],)
app.include_router(category_router, prefix="/categories", tags=["Categories"])
app.include_router(item_router, prefix='/items', tags=["Items"])

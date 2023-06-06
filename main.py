from fastapi import FastAPI

from src.endpoints.categories import category_router
from src.endpoints.subcategories import subcategory_router
from src.endpoints.menu import menu_router
from src.endpoints.restaurants import restaurant_router
from src.endpoints.dishes import item_router
from src.endpoints.compounds import compounds_router

app = FastAPI(
    title="Restaurant Assistant"
)

app.include_router(restaurant_router, prefix="/restaurants",  tags=["Restaurants"],)
app.include_router(menu_router, prefix="/menus", tags=["Menus"],)
app.include_router(category_router, prefix="/categories", tags=["Categories"])
app.include_router(subcategory_router, prefix="/subcategories", tags=["Subcategories"])
app.include_router(item_router, prefix="/items", tags=["Items"])
app.include_router(compounds_router, prefix="/compounds", tags=["Compounds"])


from fastapi import FastAPI

from src.endpoints.restaurants import restaurant_router

app = FastAPI(
    title="Restaurant Assistant"
)

app.include_router(restaurant_router, prefix="/restaurants",  tags=["Restaurants"],)

from fastapi import FastAPI
from sqlalchemy.orm import Session

from src.endpoints.restaurants import restaurant_router

app = FastAPI(
    title="Restaurant Assistant"
)

app.include_router(restaurant_router, prefix="/restaurants",  tags=["Restaurants"],)


@app.get('/{user_id}')
def get_user_id(user_id: int):
    return user_id

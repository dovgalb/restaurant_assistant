from fastapi import FastAPI
from sqlalchemy.orm import Session


app = FastAPI(
    title="Restaurant Assistant"
)


@app.get('/{user_id}')
def get_user_id(user_id: int):
    return user_id

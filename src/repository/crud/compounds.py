from src.db.models import Compounds
from src.repository.crud.base import SQLAlchemyCRUD
from src.schemas.compounds import CreateCompoundSchema, UpdateCompoundSchema


class CompoundsRepository(
    SQLAlchemyCRUD[Compounds, CreateCompoundSchema, UpdateCompoundSchema]
):
    pass


compounds_repository = CompoundsRepository(Compounds)
from typing import TypeVar

from pydantic import BaseModel  # pylint: disable = no-name-in-module

from src.db.base import Base

# Типы для обозначения моделей
ModelType = TypeVar("ModelType")
AlchemyModelType = TypeVar("AlchemyModelType", bound=Base)

# Типы для обозначения схем для создания, обновления и чтения объекта
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)

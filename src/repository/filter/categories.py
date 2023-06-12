from typing import Optional

from fastapi import Query
from sqlalchemy import BinaryExpression, and_

from src.db.models import Category
from src.repository.filter.base import SqlAlchemyFilter


class CategoryFilter(SqlAlchemyFilter):
    def __call__(
            self,
            category_id: Optional[int] = Query(default=None, example="1"),
            category_name: Optional[str] = Query(default=None, example="Кухня"),
    ) -> "CategoryFilter":

        self.category_name = category_name
        self.category_id = category_id

        return super().__call__()

    @property
    def where(self) -> Optional[BinaryExpression]:
        """Применение переданных фильтров в блоке WHERE"""
        and_args = []  # type: ignore

        if self.category_name is not None:
            and_args.append(
                self._model.name.icontains(self.category_name)
            )

        if self.category_id is not None:
            and_args.append(
                self._model.id == self.category_id
            )

        return and_(*and_args) if and_args else super().where


category_filter = CategoryFilter(Category)

"""Модуль описывает исключния, поднимаемые крудом"""
from collections.abc import Callable
from typing import Any


class DbSessionIsUnavailable(Exception):
    """Ошибка сигнализирует о недоступности сессии бд"""


def check_session(func: Callable) -> Callable:
    """Декоратор проверяет состояние бд-сессии"""

    def wrap(self, *args, **kwargs) -> Any:
        if self.db_session is None:
            raise DbSessionIsUnavailable()
        return func(self, *args, **kwargs)

    return wrap

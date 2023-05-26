from src.repository.restaurants import restaurant_repository


class RestaurantService:
    """Сервис описания операций над медиакартами субъектов РФ"""

    async def list(self) -> list[dict]:
        """Получаем список сущностей по переданным фильтрам"""
        # TODO здесь будет вызов репозитория
        repository = restaurant_repository()

        return repository.list()


def restaurant_service() -> RestaurantService:
    # TODO реализовать
    return RestaurantService()

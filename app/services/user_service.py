from app.infrastructure.database.models.user import UserModel
from app.infrastructure.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def is_registered(self, telegram_id: int) -> bool:
        user = await self._user_repository.get_by_telegram_id(telegram_id)
        return user is not None

    async def get_user(self, telegram_id: int) -> UserModel | None:
        return await self._user_repository.get_by_telegram_id(telegram_id)

    async def register_user(
        self,
        telegram_id: int,
        first_name: str,
        last_name: str,
        phone_number: str,
    ) -> UserModel:
        return await self._user_repository.create(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

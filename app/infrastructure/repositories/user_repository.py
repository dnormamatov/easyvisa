from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models.user import UserModel


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_telegram_id(self, telegram_id: int) -> UserModel | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        telegram_id: int,
        first_name: str,
        last_name: str,
        phone_number: str,
    ) -> UserModel:
        user = UserModel(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        return user

from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.infrastructure.database.session import async_session_factory
from app.infrastructure.repositories.user_repository import UserRepository
from app.infrastructure.repositories.visa_repository import VisaRepository
from app.services.user_service import UserService
from app.services.visa_service import VisaService


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with async_session_factory() as session:
            data["session"] = session
            data["user_service"] = UserService(UserRepository(session))
            data["visa_service"] = VisaService(VisaRepository(session))
            return await handler(event, data)

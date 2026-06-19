import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.bot.handlers import registration_router, start_router, visa_router
from app.bot.middlewares import DatabaseMiddleware
from app.config.settings import settings

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher(storage=MemoryStorage())

    dp.update.middleware(DatabaseMiddleware())

    dp.include_router(start_router)
    dp.include_router(registration_router)
    dp.include_router(visa_router)

    return dp


async def main() -> None:
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = create_dispatcher()

    logger.info("EasyVisa bot starting...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("EasyVisa bot stopped.")


if __name__ == "__main__":
    asyncio.run(main())
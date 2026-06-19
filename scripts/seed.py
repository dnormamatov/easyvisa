import asyncio
import logging
import sys

from app.data.seed_data import COUNTRIES, VISA_REQUIREMENTS, VISA_TYPES
from app.infrastructure.database.session import async_session_factory
from app.infrastructure.repositories.visa_repository import VisaRepository

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


async def seed() -> None:
    async with async_session_factory() as session:
        repo = VisaRepository(session)

        logger.info("Seeding countries...")
        await repo.seed_countries(COUNTRIES)

        logger.info("Seeding visa types...")
        await repo.seed_visa_types(VISA_TYPES)

        logger.info("Seeding visa requirements...")
        await repo.seed_requirements(VISA_REQUIREMENTS)

        logger.info("Seed completed successfully.")


if __name__ == "__main__":
    try:
        asyncio.run(seed())
    except Exception:
        logger.exception("Seed failed")
        sys.exit(1)

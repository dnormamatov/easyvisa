import logging

from alembic import command
from alembic.config import Config

logger = logging.getLogger(__name__)


def run_migrations() -> None:
    """Apply Alembic migrations (creates tables if they do not exist)."""
    alembic_cfg = Config("alembic.ini")
    logger.info("Running database migrations...")
    command.upgrade(alembic_cfg, "head")
    logger.info("Database migrations complete.")

"""Standalone database connection diagnostic (no bot required).

Usage:
    python -m scripts.test_db_connection
"""

from __future__ import annotations

import asyncio
import ssl
import sys
from urllib.parse import unquote, urlparse

from dotenv import load_dotenv

load_dotenv()

from app.config.settings import settings  # noqa: E402


def diagnose_url(url: str) -> None:
    print("=" * 60)
    print("DATABASE_URL diagnosis")
    print("=" * 60)

    parsed = urlparse(url)
    scheme = parsed.scheme
    host = parsed.hostname
    port = parsed.port
    username = parsed.username
    password = parsed.password
    database = (parsed.path or "").lstrip("/")

    print(f"  Scheme   : {scheme}")
    print(f"  Host     : {host}")
    print(f"  Port     : {port}")
    print(f"  Database : {database}")
    print(f"  Username : {username!r}")
    print(
        f"  Password : {'(set, length=' + str(len(unquote(password or ''))) + ')' if password else '(MISSING)'}"
    )

    issues: list[str] = []

    if scheme != "postgresql+asyncpg":
        issues.append(
            f"Expected scheme 'postgresql+asyncpg', got {scheme!r}. "
            "Plain postgresql:// URLs are auto-converted in settings."
        )

    if not password:
        issues.append(
            "Password is missing. Format: "
            "postgresql+asyncpg://postgres:<password>@db.<project>.supabase.co:5432/postgres"
        )

    if host and "pooler.supabase.com" in host:
        print("  Connection: Supabase Session Pooler")
        if port == 5432:
            print("  Mode     : Session pooler (port 5432)")
        elif port == 6543:
            print("  Mode     : Transaction pooler (port 6543)")
    elif host and host.startswith("db.") and host.endswith(".supabase.co"):
        print("  Connection: Supabase direct")

    raw = url.split("://", 1)[-1]
    if "@@" in raw:
        issues.append(
            "URL contains '@@' — password likely missing or '@' in password needs URL-encoding (%40)."
        )

    if issues:
        print("\n  ISSUES:")
        for issue in issues:
            print(f"    - {issue}")
    else:
        print("\n  URL structure looks OK.")

    print()


async def test_postgres(url: str) -> bool:
    import asyncpg

    parsed = urlparse(url)
    host = parsed.hostname or "localhost"
    port = parsed.port or 5432
    user = parsed.username or "postgres"
    password = unquote(parsed.password or "")
    database = (parsed.path or "/postgres").lstrip("/") or "postgres"

    ssl_ctx = ssl.create_default_context()

    print("Attempting asyncpg connection...")
    print(f"  -> {user}@{host}:{port}/{database} (ssl=required)")
    try:
        conn = await asyncio.wait_for(
            asyncpg.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                ssl=ssl_ctx,
            ),
            timeout=30,
        )
        version = await conn.fetchval("SELECT version()")
        await conn.close()
        print(f"  SUCCESS: {version[:80]}...")
        return True
    except asyncio.TimeoutError:
        print("  FAILED: Connection timed out (firewall/DNS/wrong host?).")
        return False
    except OSError as exc:
        print(f"  FAILED: OSError {exc!r}")
        if "121" in str(exc):
            print("  Hint: WinError 121 often means network timeout or blocked outbound port 5432.")
        return False
    except Exception as exc:
        print(f"  FAILED: {type(exc).__name__}: {exc}")
        return False


async def test_sqlalchemy(url: str) -> bool:
    from sqlalchemy import text
    from sqlalchemy.ext.asyncio import create_async_engine

    engine = create_async_engine(
        url,
        connect_args={"ssl": ssl.create_default_context()},
        pool_pre_ping=True,
    )
    print("Attempting SQLAlchemy engine connection...")
    try:
        async with asyncio.timeout(30):
            async with engine.connect() as conn:
                result = await conn.execute(text("SELECT 1"))
                value = result.scalar()
        await engine.dispose()
        print(f"  SUCCESS: SELECT 1 => {value}")
        return True
    except asyncio.TimeoutError:
        print("  FAILED: SQLAlchemy connection timed out.")
        await engine.dispose()
        return False
    except OSError as exc:
        print(f"  FAILED: OSError {exc!r}")
        await engine.dispose()
        return False
    except Exception as exc:
        print(f"  FAILED: {type(exc).__name__}: {exc}")
        await engine.dispose()
        return False


async def main() -> int:
    url = settings.database_url
    diagnose_url(url)

    if not url.startswith("postgresql"):
        print(f"Unsupported DATABASE_URL scheme: {url.split('://', 1)[0]}")
        return 1

    pg_ok = await test_postgres(url)
    sa_ok = await test_sqlalchemy(url)
    ok = pg_ok and sa_ok

    print()
    if ok:
        print("All connection tests passed.")
        return 0
    print("Connection tests failed. See issues above.")
    return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

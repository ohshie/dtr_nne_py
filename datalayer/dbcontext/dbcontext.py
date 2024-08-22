import os
import shutil

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from core.config import settings


def get_db_session():
    db_path = settings.db_location
    if settings.python_env == "test":
        if not os.path.exists(settings.db_location) or os.path.getatime(
            settings.test_db_location
        ) > os.path.getmtime(settings.db_location):
            shutil.copy2(settings.db_location, settings.test_db_location)

    engine = create_async_engine(f"{settings.db_connection_string}{db_path}")
    session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    return session()

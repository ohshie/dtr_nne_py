import os
import shutil

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from core.config import settings


def get_db_session():
    db_path = settings.prod_db_location
    if settings.python_env == "test":
        if not os.path.exists(settings.debug_db_location):
            source_db = os.path.abspath(settings.prod_db_location)
            shutil.copy2(source_db, settings.debug_db_location)
        db_path = settings.debug_db_location

    engine = create_async_engine(f"{settings.db_connection_string}{db_path}")
    session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    return session()

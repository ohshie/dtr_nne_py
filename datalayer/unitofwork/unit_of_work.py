import logging

from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession

from datalayer.dbcontext.dbcontext import get_db_session


class UnitOfWork:
    def __init__(self):
        self.session: AsyncSession = get_db_session()
        self.logger = logging.getLogger(self.__class__.__name__)
        self._locked_tables = set()

    async def __aenter__(self):
        self.transaction = self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.logger.error(f"Error occurred {exc_type}. Rolling back")
            await self.session.rollback()
        else:
            try:
                await self.session.commit()
            except Exception as e:
                self.logger.error(f"Error occurred during commit: {e}. Rolling back")
                await self.session.rollback()
                await self.session.close()
                raise
            finally:
                await self._release_all_locks()
                await self.session.close()

    async def commit(self):
        await self.session.commit()

    @property
    def commited(self):
        return not self.session.is_active

    async def lock_table(self, table_name: str, timeout: int = 10):
        if table_name in self._locked_tables:
            return

        try:
            await self.session.execute(text("BEGIN IMMEDIATE TRANSACTION"))
            await self.session.execute(text(f"SELECT * FROM {table_name} LIMIT 1"))
            self._locked_tables.add(table_name)
            self.logger.info(f"Aquired lock for table {table_name}")
        except OperationalError as e:
            if "database is locked" in str(e):
                self.logger.error(
                    f"Failed to acquire lock for table {table_name}: database is locked"
                )
            else:
                self.logger.error(
                    f"Error occurred while locking table {table_name}: {e}"
                )
            raise

    async def _release_all_locks(self):
        self._locked_tables.clear()
        self.logger.info("Released all locks")

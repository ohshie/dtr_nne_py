import logging

from sqlalchemy.ext.asyncio import AsyncSession

from datalayer.dbcontext.dbcontext import get_db_session


class UnitOfWork:
    def __init__(self):
        self.session: AsyncSession = get_db_session()
        self.logger = logging.getLogger(self.__class__.__name__)

    async def __aenter__(self):
        self.transaction = self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.logger.error(f"Error occurred {exc_type}. Rolling back")
            await self.session.rollback()
        else:
            try:
                await self.session.close()
            except Exception as e:
                self.logger.error(f"Error occurred during commit: {e}. Rolling back")
                await self.session.rollback()
                await self.session.close()
                raise

    async def commit(self):
        await self.session.commit()

    @property
    def commited(self):
        return not self.session.is_active

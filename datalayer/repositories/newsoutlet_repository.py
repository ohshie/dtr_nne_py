import logging

from httpx import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import delete

from datalayer.repositories.generic_repository import GenericRepository
from models.domainmodels.newsoutlet import NewsOutlet
from datalayer.unitofwork.unit_of_work import UnitOfWork


class NewsOutletRepository(GenericRepository[NewsOutlet]):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow.session, NewsOutlet)
        self.uow = uow
        self.logger = logging.getLogger(self.__class__.__name__)

    async def batch_edit(self, entities: list[NewsOutlet]) -> bool:
        try:
            for entity in entities:
                await self.session.merge(entity)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error updating entities: {str(e)}")
            return False

    async def clear_table(self):
        try:
            stmt = delete(NewsOutlet)
            await self.session.execute(stmt)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error clearing table: {str(e)}")
            return False

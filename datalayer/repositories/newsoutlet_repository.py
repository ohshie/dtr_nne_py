import logging

from sqlalchemy.exc import SQLAlchemyError

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
            self.session.merge(entities)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error updating entities: {str(e)}")
            return False

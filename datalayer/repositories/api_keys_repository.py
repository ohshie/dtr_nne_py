import logging
from typing import TypeVar, Generic

from sqlalchemy import select

from datalayer.repositories.generic_repository import GenericRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork

T = TypeVar("T")


class ApiKeyRepository(GenericRepository[T]):
    def __init__(self, uow: UnitOfWork, api_service: Generic[T]):
        super().__init__(uow.session, api_service)
        self._uow = uow
        self._api_service = api_service
        self.logger = logging.getLogger(self.__class__.__name__)

    async def get_default(self) -> Generic[T]:
        result = await self.session.execute(select(self.model))
        api_service = result.scalar()

        return api_service

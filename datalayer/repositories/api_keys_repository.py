import logging
from typing import TypeVar, Generic

from datalayer.repositories.generic_repository import GenericRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork

T = TypeVar("T")


class ApiKeyRepository(GenericRepository[T]):
    def __init__(self, uow: UnitOfWork, api_service: Generic[T]):
        super().__init__(uow.session, api_service)
        self._uow = uow
        self.logger = logging.getLogger(self.__class__.__name__)

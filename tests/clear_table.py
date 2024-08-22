from typing import Generic, TypeVar

from datalayer.repositories.api_keys_repository import ApiKeyRepository
from datalayer.repositories.newsoutlet_repository import NewsOutletRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.deepl import Deepl
from models.domainmodels.newsoutlet import NewsOutlet
from models.domainmodels.zenrows import Zenrows

T = TypeVar("T")


async def clear_table(table: Generic[T]):
    async with UnitOfWork() as uow:
        if table == NewsOutlet:
            repository = NewsOutletRepository(uow)
        if table == Zenrows:
            repository = ApiKeyRepository(uow, Zenrows)
        if table == Deepl:
            repository = ApiKeyRepository(uow, Deepl)

        await repository.clear_table()
        await uow.commit()

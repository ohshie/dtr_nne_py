from datalayer.repositories.api_keys_repository import ApiKeyRepository
from datalayer.repositories.newsoutlet_repository import NewsOutletRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.deepl import Deepl
from models.domainmodels.zenrows import Zenrows


async def clear_table(table: str):
    async with UnitOfWork() as uow:
        if table == "newsoutlet":
            repository = NewsOutletRepository(uow)
        if table == "zenrows":
            repository = ApiKeyRepository(uow, Zenrows)
        if table == "deepl":
            repository = ApiKeyRepository(uow, Deepl)

        await repository.clear_table()
        await uow.commit()

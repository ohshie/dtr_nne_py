import pytest

from datalayer.repositories.api_keys_repository import ApiKeyRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.zenrows import Zenrows


@pytest.mark.asyncio
async def test_connection():
    async with UnitOfWork() as uow:
        await uow.lock_table(Zenrows)
        api_key_repository = ApiKeyRepository(uow, Zenrows)

        api_keys: list[Zenrows] = await api_key_repository.get_all()

        assert len(api_keys) == 1

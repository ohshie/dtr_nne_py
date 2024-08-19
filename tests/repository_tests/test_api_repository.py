import pytest

from datalayer.repositories.api_keys_repository import ApiKeyRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.deepl import Deepl


@pytest.mark.asyncio
async def test_connection():
    async with UnitOfWork() as uow:

        api_key_repository = ApiKeyRepository(uow, Deepl)

        api_keys: list[Deepl] = await api_key_repository.get_all()

        assert len(api_keys) == 0

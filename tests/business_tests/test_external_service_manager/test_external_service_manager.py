import pytest

from business.external_service_manager.external_service_manager import (
    provide_current_key,
    set_new_api_key,
    update_api_key,
)
from core.config import settings
from models.domainmodels.zenrows import Zenrows
from tests.clear_table import clear_table


@pytest.mark.asyncio
async def test_get_current_service_api_key():
    await clear_table(Zenrows)
    await set_new_api_key(Zenrows, settings.zenrows_test_key)

    current_api_key = await provide_current_key(Zenrows)

    assert current_api_key is not None
    assert isinstance(current_api_key, Zenrows)
    assert current_api_key.ApiKey != ""


@pytest.mark.asyncio
async def test_set_new_service_api_key():
    await clear_table(Zenrows)

    success = await set_new_api_key(Zenrows, settings.zenrows_test_key)

    assert success


@pytest.mark.asyncio
async def test_set_new_service_api_key_invalid():
    return


@pytest.mark.asyncio
async def test_update_new_service_api_key_base():
    await clear_table(Zenrows)
    await set_new_api_key(Zenrows, settings.zenrows_test_key)

    success = await update_api_key(Zenrows, settings.zenrows_test_key)

    assert success

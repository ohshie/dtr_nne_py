import pytest
from business.external_service_manager.check_external_service_key_manager import (
    check_service_key_validity,
    check_zenrows_key_validity,
    check_deepl_key_validity,
    check_chatgpt_key_validity,
)
from core.config import settings
from models.domainmodels.chatgptmodel import ChatGptModel
from models.domainmodels.deepl import Deepl
from models.domainmodels.newsoutlet import NewsOutlet
from models.domainmodels.zenrows import Zenrows


@pytest.mark.asyncio
async def test_check_service_key_validity_base():
    zenrows_model = Zenrows(ApiKey=settings.zenrows_test_key)

    success = await check_service_key_validity(Zenrows, zenrows_model)

    assert success


@pytest.mark.asyncio
async def test_check_service_key_validity_zenrows_empty():

    success = await check_service_key_validity(Zenrows, None)

    assert not success


@pytest.mark.asyncio
async def test_check_service_key_validity_zenrows_wrong_class():
    zenrows_model = Zenrows(ApiKey=settings.zenrows_test_key)

    success = await check_service_key_validity(NewsOutlet, zenrows_model)

    assert not success


@pytest.mark.asyncio
async def test_check_service_key_validity_zenrows_none_api_key():
    zenrows_model = Zenrows(ApiKey=None)

    success = await check_service_key_validity(Zenrows, zenrows_model)

    assert not success


@pytest.mark.asyncio
async def test_check_service_key_validity_zenrows_empty_api_key():
    zenrows_model = Zenrows(ApiKey="")

    success = await check_service_key_validity(Zenrows, zenrows_model)

    assert not success


@pytest.mark.asyncio
async def test_check_zenrows_key_validity_base():
    zenrows_model = Zenrows(ApiKey=settings.zenrows_test_key)

    success = await check_zenrows_key_validity(zenrows_model)

    assert success


@pytest.mark.asyncio
async def test_check_zenrows_key_validity_invalid_key():
    zenrows_model = Zenrows(ApiKey="settings.zenrows_test_key")

    success = await check_zenrows_key_validity(zenrows_model)

    assert not success


@pytest.mark.asyncio
async def test_check_deepl_key_validity_base():
    deepl_model = Deepl(ApiKey=settings.deepl_test_key)

    success = await check_deepl_key_validity(deepl_model)

    assert success


@pytest.mark.asyncio
async def test_check_deepl_key_validity_invalid_key():
    deepl_model = Deepl(ApiKey="")

    success = await check_deepl_key_validity(deepl_model)

    assert not success


@pytest.mark.asyncio
async def test_check_chatgpt_key_validity_base():
    chatgpt_model = ChatGptModel(ApiKey=settings.chatgpt_test_key)

    success = await check_chatgpt_key_validity(chatgpt_model)

    assert success

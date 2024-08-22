from __future__ import annotations

import logging
from typing import TypeVar, Generic, Union

from business.external_service_manager.check_external_service_key_manager import (
    check_service_key_validity,
)
from datalayer.repositories.api_keys_repository import ApiKeyRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.chatgptmodel import ChatGptModel
from models.domainmodels.deepl import Deepl
from models.domainmodels.zenrows import Zenrows

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Union[Zenrows, ChatGptModel, Deepl])


async def provide_current_key(model: Generic[T]):
    logger.info(f"Getting current stored Api key of {model}")

    async with UnitOfWork() as uow:
        await uow.lock_table(model)
        repository = ApiKeyRepository(uow, model)

        current_api_key = await repository.get_default()
        if current_api_key is None or "":
            logger.warning(f"Empty Api key in {model}")

    return current_api_key


async def set_new_api_key(model: Generic[T], api_key: str) -> str | bool:
    logger.info(f"Setting new Api key of {model}")

    model.ApiKey = api_key

    valid = await check_service_key_validity(model, model)
    if not valid:
        return "Invalid api key"

    async with UnitOfWork() as uow:
        await uow.lock_table(model)
        repository = ApiKeyRepository(uow, model)

        service_api_key = model(
            ApiKey=api_key,
        )

        success = await repository.add(service_api_key)

        await uow.commit()

    return success


async def update_api_key(model: Generic[T], new_api_key: str):
    logger.info(f"Updating Api key of {model}")

    async with UnitOfWork() as uow:
        await uow.lock_table(model)
        repository = ApiKeyRepository(uow, model)

        current_entity = await repository.get_default()

        current_entity.ApiKey = new_api_key

        success = await repository.update(current_entity)

        if not success:
            logger.error("failed to update api key with new value")
            return False

        await uow.commit()

    return success

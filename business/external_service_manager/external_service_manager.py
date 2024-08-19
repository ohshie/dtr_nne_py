import logging
from typing import TypeVar, Generic

logger = logging.getLogger(__name__)

T = TypeVar("T")


async def ProvideCurrentKey(model: Generic[T]):
    logger.info(f"Getting current stored Api key of {model}")

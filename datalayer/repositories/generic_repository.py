from __future__ import annotations

import logging
from typing import Generic, TypeVar

from sqlalchemy.engine import Result
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class GenericRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: T):
        self.session = session
        self.model = model
        self.logger = logging.getLogger(self.__class__.__name__)

    async def get(self, entity_id: int) -> T | None:
        return await self.session.get(self.model, entity_id)

    async def get_all(self) -> list[T]:
        query = select(self.model)
        result: Result = await self.session.execute(query)
        entities = result.scalars().all()
        return list(entities)

    async def add(self, entity: T) -> bool:
        if entity is None:
            return False
        try:
            self.session.add(entity)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error adding new entity: {str(e)}")
            return False

    async def batch_add(self, entities: list[T]) -> bool:
        try:
            self.session.add_all(entities)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error adding new entities: {str(e)}")
            return False

    async def update(self, entity: T) -> bool:
        if entity is None:
            return False
        try:
            await self.session.merge(entity)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error updating entity: {str(e)}")
            return False

    async def remove(self, entity: T) -> bool:
        if entity is None:
            return False
        try:
            await self.session.delete(entity)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error removing entity: {str(e)}")
            return False

    async def clear_table(self):
        try:
            stmt = delete(self.model)
            await self.session.execute(stmt)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error clearing table: {str(e)}")
            return False

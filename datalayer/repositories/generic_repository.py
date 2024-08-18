import logging
import re
from typing import Generic, TypeVar

from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class GenericRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: T):
        self.session = session
        self.model = model
        self.logger = logging.getLogger(self.__class__.__name__)

    async def get(self, id: int) -> T:
        query = select(self.model).filter(id == self.model.id)
        result: Result = await self.session.execute(query)
        entity = result.scalar().one_or_none()
        return entity

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

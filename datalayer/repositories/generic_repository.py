import logging
from typing import Generic, TypeVar
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

T = TypeVar("T")


class GenericRepository(Generic[T]):
    def __init__(self, session: Session, model: T):
        self.session = session
        self.model = model
        self.logger = logging.getLogger(self.__class__.__name__)

    async def get(self, id: int) -> T:
        return await self.session.query(self.model).filter(self.model.id == id).first()

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
            self.session.merge(entity)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error updating entity: {str(e)}")
            return False

    async def remove(self, entity: T) -> bool:
        if entity is None:
            return False
        try:
            self.session.delete(entity)
            return True
        except SQLAlchemyError as e:
            self.logger.error(f"Error removing entity: {str(e)}")
            return False

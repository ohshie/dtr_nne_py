from sqlalchemy.orm import Session
import logging

class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.logger = logging.getLogger(self.__class__.__name__)

    async def __aenter__(self):
        self.transaction = self.session.begin_nested()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.logger.error(f"Error occurred {exc_type}. Rolling back")
            self.transaction.rollback()
        else:
            try:
                self.transaction.commit()
            except Exception as e:
                self.logger.error(f"Error occurred during commit: {e}. Rolling back")
                self.transaction.rollback()
                raise

    @property
    def commited(self):
        return not self.transaction.is_active
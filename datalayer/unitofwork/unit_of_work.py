import logging

from datalayer.dbcontext.dbcontext import get_db_session


class UnitOfWork:
    def __init__(self):
        self.session = get_db_session()
        self.logger = logging.getLogger(self.__class__.__name__)

    async def __aenter__(self):
        self.transaction = self.session
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

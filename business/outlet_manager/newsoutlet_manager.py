from datalayer.repositories.newsoutlet_repository import NewsOutletRepository
from mappers.newsoutlet_mapper import map_newsoutlet_dto_to_domain, map_domainoutlets_to_DTO
from datalayer.unitofwork.unit_of_work import UnitOfWork
from datalayer.dbcontext.dbcontext import get_db_session
from models.dto.newsoutlet_dto import NewsOutletDTO
import logging

async def add_new_outlet(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutletDTO]:
    session = get_db_session()

    async with UnitOfWork(session) as uow:
        newsoutlet_repository = NewsOutletRepository(uow)

        logging.info(f"Received {len(outlets_dto)} outlets to add. Starting to map DTO to Domain models")

        mapped_outlets = map_newsoutlet_dto_to_domain(outlets_dto)

        logging.info(f"Mapped a total of: {len(mapped_outlets)} outlets. Passing them to Db")

        success = await newsoutlet_repository.batch_add(mapped_outlets)
        if success is False:
            logging.error("Failed to add outlets to database")
            return []

        added_outlets = mapped_outlets

        logging.info(f"Added {len(added_outlets)} outlets to DB. Starting to map them to DTO")

        mapped_new_outlets_dto = map_domainoutlets_to_DTO(added_outlets)

        logging.info(f"Mapped a total of {len(mapped_new_outlets_dto)} outlets to DTO")

        return mapped_new_outlets_dto
from datalayer.repositories.newsoutlet_repository import NewsOutletRepository
from helpers.duplicates_manager import filter_duplicates
from mappers.newsoutlet_mapper import (
    map_newsoutlet_dto_to_domain,
    map_domainoutlets_to_DTO,
)
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO
import logging


async def add_new_outlet(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutletDTO]:
    mapped_outlets = map_newsoutlet_dto_to_domain(outlets_dto)

    async with UnitOfWork() as uow:
        newsoutlet_repository = NewsOutletRepository(uow)

        saved_outlets = await newsoutlet_repository.get_all()

        success = await newsoutlet_repository.batch_add(mapped_outlets)
        if success is False:
            logging.error("Failed to add outlets to database")
            return []

    added_outlets = mapped_outlets

    logging.info(
        f"Added {len(added_outlets)} outlets to DB. Starting to map them to DTO"
    )

    mapped_new_outlets_dto = map_domainoutlets_to_DTO(added_outlets)

    logging.info(f"Mapped a total of {len(mapped_new_outlets_dto)} outlets to DTO")

    return mapped_new_outlets_dto


async def edit_existing_outlet(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutletDTO]:
    return []


def map_and_filter_incoming(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutlet]:
    if len(outlets_dto) < 1:
        logging.info("Received empty list of outlets dto. Returning empty list")
        return []
    else:
        logging.info(
            f"Received {len(outlets_dto)} outlets to add. Starting to map DTO to Domain models"
        )

    outlets_dto = filter_duplicates(outlets_dto)

    mapped_outlets = map_newsoutlet_dto_to_domain(outlets_dto)
    if len(mapped_outlets) != len(outlets_dto):
        logging.error(
            "Amount of mapped outlets is less than incoming outlet DTO's, please double check provided outlets"
        )
        return []
    else:
        logging.info(
            f"Mapped a total of: {len(mapped_outlets)} outlets. Passing them to Db"
        )

    return mapped_outlets

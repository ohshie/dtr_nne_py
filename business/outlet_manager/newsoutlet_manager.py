from datalayer.repositories.newsoutlet_repository import NewsOutletRepository
from helpers.duplicates_helper import filter_duplicates, find_uniques
from helpers.validity_helper import is_valid_outlet_object
from mappers.newsoutlet_mapper import (
    map_newsoutlet_dto_to_domain,
    map_domainoutlets_to_DTO,
)
from datalayer.unitofwork.unit_of_work import UnitOfWork
from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO
import logging


async def add_new_outlet(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutletDTO]:
    prepared_outlets = map_filter_verify_incoming(outlets_dto)
    if prepared_outlets is []:
        return []

    async with UnitOfWork() as uow:
        newsoutlet_repository = NewsOutletRepository(uow)

        saved_outlets = await newsoutlet_repository.get_all()
        outlets_to_be_added = find_uniques(saved_outlets, prepared_outlets)
        if len(outlets_to_be_added) > 0:
            success = await newsoutlet_repository.batch_add(outlets_to_be_added)
            if success is False:
                logging.error("Failed to add outlets to database")
                return []
        else:
            logging.info("All incoming outlets already present in db")
            return []

    added_outlets = outlets_to_be_added

    logging.info(
        f"Added {len(added_outlets)} outlets to DB. Starting to map them to DTO"
    )

    mapped_new_outlets_dto = map_domainoutlets_to_DTO(added_outlets)

    logging.info(f"Mapped a total of {len(mapped_new_outlets_dto)} outlets to DTO")

    return mapped_new_outlets_dto


async def edit_existing_outlet(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutletDTO]:
    return mapped_edited_outlets_dto


def map_filter_verify_incoming(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutlet]:
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
            f"Mapped a total of: {len(mapped_outlets)} outlets. Passing them to verificator"
        )

    verified_outlets = check_outlets(mapped_outlets)
    if len(verified_outlets) != len(mapped_outlets):
        logging.error(
            "Some outlets did not pass verification. Please double check provided outlets"
        )
        return []
    else:
        logging.info("Passing verified outlets to Db")

    return verified_outlets


def check_outlets(outlets: list[NewsOutlet]) -> list[NewsOutlet]:
    return [outlet for outlet in outlets if is_valid_outlet_object(outlet)]

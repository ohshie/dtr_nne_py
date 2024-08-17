import pytest

from business.outlet_manager.newsoutlet_manager import add_new_outlet
from .make_requests import post_request
from models.dto.newsoutlet_dto import NewsOutletDTO
from models.domainmodels.newsoutlet import NewsOutlet
from mappers.newsoutlet_mapper import (
    map_newsoutlet_dto_to_domain,
    map_domainoutlets_to_DTO,
)

test_outlets_DTO = [
    NewsOutletDTO(
        inUse=True,
        alwaysJs=False,
        name="first_outlet",
        website="website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
    NewsOutletDTO(
        inUse=True,
        alwaysJs=False,
        name="second_outlet",
        website="website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
]

test_outlets: list[NewsOutlet] = [
    NewsOutlet(
        id=1,
        inUse=True,
        alwaysJs=False,
        name="first_outlet",
        website="website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
    NewsOutlet(
        id=2,
        inUse=True,
        alwaysJs=False,
        name="second_outlet",
        website="website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
]


def test_add_newsoutlet_api():
    response = post_request("/AddNewOutlet", test_outlets_DTO)

    assert response.status_code == 201


def test_newsoutlet_mapper():
    domain_outlets = map_newsoutlet_dto_to_domain(test_outlets_DTO)

    assert isinstance(domain_outlets, list)
    assert len(domain_outlets) > 0
    assert all(isinstance(outlet, NewsOutlet) for outlet in domain_outlets)


def test_newsoutlet_DTO_mapper():
    outlets_DTO = map_domainoutlets_to_DTO(test_outlets)

    assert isinstance(outlets_DTO, list)
    assert len(outlets_DTO) > 0
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in outlets_DTO)


@pytest.mark.asyncio
async def test_add_newsoutlet_manager():
    outlets_DTO = await add_new_outlet(test_outlets_DTO)

    assert isinstance(outlets_DTO, list)
    assert len(outlets_DTO) > 0
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in outlets_DTO)

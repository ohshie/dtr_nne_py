from mappers.newsoutlet_mapper import (
    map_newsoutlet_dto_to_domain,
    map_domainoutlets_to_DTO,
)
from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_correct_1,
    mock_newsoutlet_correct_1,
    mock_newsoutlet_DTO_correct_2,
    mock_newsoutlet_correct_2,
)


def test_newsoutlet_mapper():
    outlets_dto_list: list[NewsOutletDTO] = [
        mock_newsoutlet_DTO_correct_1,
        mock_newsoutlet_DTO_correct_2,
    ]
    domain_outlets = map_newsoutlet_dto_to_domain(outlets_dto_list)

    assert isinstance(domain_outlets, list)
    assert len(domain_outlets) > 0
    assert all(isinstance(outlet, NewsOutlet) for outlet in domain_outlets)


def test_newsoutlet_DTO_mapper():
    outlets_list: list[NewsOutlet] = [
        mock_newsoutlet_correct_1,
        mock_newsoutlet_correct_2,
    ]

    outlets_DTO = map_domainoutlets_to_DTO(outlets_list)

    assert isinstance(outlets_DTO, list)
    assert len(outlets_DTO) > 0
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in outlets_DTO)

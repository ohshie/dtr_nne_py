from mappers.newsoutlet_mapper import (
    map_newsoutlet_dto_to_domain,
    map_domainoutlets_to_DTO,
)
from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_factory,
    mock_newsoutlet_DTO_list_factory,
    mock_newsoutlet_list_factory,
)


def test_newsoutlet_mapper():
    domain_outlets = map_newsoutlet_dto_to_domain(mock_newsoutlet_DTO_list_factory(2))

    assert isinstance(domain_outlets, list)
    assert len(domain_outlets) > 0
    assert all(isinstance(outlet, NewsOutlet) for outlet in domain_outlets)


def test_newsoutlet_DTO_mapper():
    outlets_DTO = map_domainoutlets_to_DTO(mock_newsoutlet_list_factory(2))

    assert isinstance(outlets_DTO, list)
    assert len(outlets_DTO) > 0
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in outlets_DTO)

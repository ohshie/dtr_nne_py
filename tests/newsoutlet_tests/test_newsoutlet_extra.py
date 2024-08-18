from business.outlet_manager.newsoutlet_manager import map_filter_verify_incoming
from mappers.newsoutlet_mapper import (
    map_domainoutlets_to_DTO,
)

from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_list_factory,
    mock_newsoutlet_DTO_factory,
)


def test_map_filter_verify_incoming_emptylist():
    prepared_outlets = map_domainoutlets_to_DTO([])

    assert isinstance(prepared_outlets, list)
    assert len(prepared_outlets) == len([])


def test_map_filter_verify_incoming_faultylist():
    faulty_outlets = mock_newsoutlet_DTO_list_factory(2)
    faulty_outlets.append(mock_newsoutlet_DTO_factory(correct=False))

    prepared_outlets = map_filter_verify_incoming(faulty_outlets, "test")
    assert isinstance(prepared_outlets, list)
    assert len(prepared_outlets) < len(faulty_outlets)

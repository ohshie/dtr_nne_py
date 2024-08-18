from business.outlet_manager.newsoutlet_manager import map_filter_verify_incoming
from mappers.newsoutlet_mapper import (
    map_domainoutlets_to_DTO,
)

from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_correct_1,
    mock_newsoutlet_DTO_correct_2,
    mock_newsoutlet_DTO_invalidurl,
)


def test_map_filter_verify_incoming_emptylist():
    prepared_outlets = map_domainoutlets_to_DTO([])

    assert isinstance(prepared_outlets, list)
    assert len(prepared_outlets) == len([])


def test_map_filter_verity_incoming_faultylist():
    faulty_outlets = [
        mock_newsoutlet_DTO_correct_1,
        mock_newsoutlet_DTO_correct_2,
        mock_newsoutlet_DTO_correct_1,
        mock_newsoutlet_DTO_invalidurl,
    ]

    prepared_outlets = map_filter_verify_incoming(faulty_outlets)
    assert isinstance(prepared_outlets, list)
    assert len(prepared_outlets) < len(faulty_outlets)

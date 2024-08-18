from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.make_requests import post_request
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_correct_1,
    mock_newsoutlet_DTO_correct_2,
)


def test_add_newsoutlet_api():
    outlets_dto_list: list[NewsOutletDTO] = [
        mock_newsoutlet_DTO_correct_1,
        mock_newsoutlet_DTO_correct_2,
    ]

    response = post_request("/AddNewOutlet", outlets_dto_list)

    assert response.status_code == 201

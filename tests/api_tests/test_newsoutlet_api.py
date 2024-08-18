from concurrent.futures import ThreadPoolExecutor

import pytest

from business.outlet_manager.newsoutlet_manager import add_new_outlet
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.make_requests import post_request, get_request, put_request, delete_request
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_factory,
    mock_newsoutlet_DTO_list_factory,
)
from tests.newsoutlet_tests.clear_newsoutlets_table import clear_newsoutlets_table


@pytest.mark.asyncio
async def test_get_newsoulet_api_base():
    await clear_newsoutlets_table()

    mock_outlets_DTO_list = mock_newsoutlet_DTO_list_factory(2)
    await add_new_outlet(mock_outlets_DTO_list)

    response = get_request("/GetCurrentOutlets")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_newsoulet_api_empty():
    await clear_newsoutlets_table()

    response = get_request("/GetCurrentOutlets")

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_add_newsoutlet_api_base():
    await clear_newsoutlets_table()

    mock_outlets_DTO_list = mock_newsoutlet_DTO_list_factory(2)

    response = post_request("/AddNewOutlet", mock_outlets_DTO_list)

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_add_newsoutlet_api_faulty():

    response = post_request(
        "/AddNewOutlet", [mock_newsoutlet_DTO_factory(correct=False)]
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_add_newsoutlet_api_empty():
    response = post_request("/AddNewOutlet", [])

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_add_newsoutlet_api_concurrency():
    await clear_newsoutlets_table()

    payloads = [
        [mock_newsoutlet_DTO_factory(), mock_newsoutlet_DTO_factory()],
        [mock_newsoutlet_DTO_factory(), mock_newsoutlet_DTO_factory()],
        [mock_newsoutlet_DTO_factory(), mock_newsoutlet_DTO_factory()],
    ]

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(post_request, "/AddNewOutlet", payload)
            for payload in payloads
        ]
        responses = [future.result() for future in futures]

    for response in responses:
        assert response.status_code == 201


@pytest.mark.asyncio
async def test_edit_newsoutlet_api_base():
    await clear_newsoutlets_table()

    mock_newsoutlet_DTO_list: list[NewsOutletDTO] = mock_newsoutlet_DTO_list_factory(2)

    await add_new_outlet(mock_newsoutlet_DTO_list)

    mock_newsoutlet_DTO_list[0].name = "New name"

    edited_outlets = put_request("/UpdateNewsOutlet", [mock_newsoutlet_DTO_list[0]])

    assert edited_outlets.status_code == 200


@pytest.mark.asyncio
async def test_edit_newsoutlet_api_faulty():
    await clear_newsoutlets_table()

    mock_newsoutlet_DTO_list = mock_newsoutlet_DTO_list_factory(2)

    await add_new_outlet(mock_newsoutlet_DTO_list)

    mock_newsoutlet_DTO_list[0].website = "invalid url"

    edited_outlets = put_request("/UpdateNewsOutlet", [mock_newsoutlet_DTO_list[0]])

    assert edited_outlets.status_code == 400


@pytest.mark.asyncio
async def test_edit_newsoutlet_api_empty():
    await clear_newsoutlets_table()

    edited_outlets = put_request("/UpdateNewsOutlet", [mock_newsoutlet_DTO_factory()])

    assert edited_outlets.status_code == 400


@pytest.mark.asyncio
async def test_delete_newsoutlet_api_base():
    await clear_newsoutlets_table()
    mock_newsoutlet_DTO_list = mock_newsoutlet_DTO_list_factory(2)
    await add_new_outlet(mock_newsoutlet_DTO_list)

    deleted_outlets = delete_request("/DeleteNewsOutlet", mock_newsoutlet_DTO_list)

    assert deleted_outlets.status_code == 200


@pytest.mark.asyncio
async def test_delete_newsoutlet_api_faulty():
    await clear_newsoutlets_table()
    mock_newsoutlet_DTO_list = mock_newsoutlet_DTO_list_factory(2)
    await add_new_outlet(mock_newsoutlet_DTO_list)

    mock_newsoutlet_DTO_list[0].website = "invalid url"

    deleted_outlets = delete_request("/DeleteNewsOutlet", mock_newsoutlet_DTO_list)

    assert deleted_outlets.status_code == 400


@pytest.mark.asyncio
async def test_delete_newsoutlet_api_empty():
    await clear_newsoutlets_table()

    deleted_outlets = delete_request(
        "/DeleteNewsOutlet", [mock_newsoutlet_DTO_factory(2)]
    )

    assert deleted_outlets.status_code == 400

import copy

import pytest

from business.outlet_manager.newsoutlet_manager import (
    edit_existing_outlet,
    add_new_outlet,
)
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_correct_1,
    mock_newsoutlet_DTO_correct_2,
    mock_newsoutlet_DTO_invalidurl,
)
from tests.newsoutlet_tests.clear_newsoutlets_table import clear_newsoutlets_table

mock_edited_outlet_DTO = copy.copy(mock_newsoutlet_DTO_correct_1)
mock_edited_outlet_DTO.name = "changed name"


@pytest.mark.asyncio
async def test_edit_existing_outlet_base():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1])

    edited_outlet = await edit_existing_outlet([mock_edited_outlet_DTO])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 1
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in edited_outlet)


@pytest.mark.asyncio
async def test_edit_existing_outlet_empty():
    await clear_newsoutlets_table()
    edited_outlet = await edit_existing_outlet([])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 0


@pytest.mark.asyncio
async def test_edit_existing_outlet_notfound():
    await clear_newsoutlets_table()

    edited_outlet = await edit_existing_outlet([mock_newsoutlet_DTO_correct_1])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 0


@pytest.mark.asyncio
async def test_edit_existing_outlet_duplicate():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2])

    edited_outlet = await edit_existing_outlet(
        [mock_edited_outlet_DTO, mock_edited_outlet_DTO]
    )

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 1


@pytest.mark.asyncio
async def test_edit_existing_outlet_duplicate_name():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1])

    faulty_mock_edited_outlet = copy.copy(mock_edited_outlet_DTO)
    faulty_mock_edited_outlet.website = mock_newsoutlet_DTO_invalidurl.website

    edited_outlet = await edit_existing_outlet([faulty_mock_edited_outlet])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 0

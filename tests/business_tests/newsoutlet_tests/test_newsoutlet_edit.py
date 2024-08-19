import pytest

from business.outlet_manager.newsoutlet_manager import (
    edit_existing_outlet,
    add_new_outlet,
)
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_factory,
    mock_newsoutlet_DTO_list_factory,
)
from tests.clear_table import clear_table


@pytest.mark.asyncio
async def test_edit_existing_outlet_base():
    await clear_table("newsoutlet")

    mock_newsoutlet_DTO = mock_newsoutlet_DTO_factory()

    await add_new_outlet([mock_newsoutlet_DTO])

    mock_newsoutlet_DTO.name = "Changed name"

    edited_outlet = await edit_existing_outlet([mock_newsoutlet_DTO])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 1
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in edited_outlet)


@pytest.mark.asyncio
async def test_edit_existing_outlet_empty():
    await clear_table("newsoutlet")
    edited_outlet = await edit_existing_outlet([])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 0


@pytest.mark.asyncio
async def test_edit_existing_outlet_notfound():
    await clear_table("newsoutlet")

    edited_outlet = await edit_existing_outlet([mock_newsoutlet_DTO_factory()])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 0


@pytest.mark.asyncio
async def test_edit_existing_outlet_duplicate():
    await clear_table("newsoutlet")

    mock_newsoulet_DTO_list = mock_newsoutlet_DTO_list_factory(2)

    await add_new_outlet(mock_newsoulet_DTO_list)

    mock_newsoulet_DTO_list[0].name = "Changed name"

    edited_outlet = await edit_existing_outlet(
        [mock_newsoulet_DTO_list[0], mock_newsoulet_DTO_list[0]]
    )

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 1


@pytest.mark.asyncio
async def test_edit_existing_outlet_faulty():
    await clear_table("newsoutlet")

    mock_newsoutlet_DTO = mock_newsoutlet_DTO_factory()

    await add_new_outlet([mock_newsoutlet_DTO])

    mock_newsoutlet_DTO.website = "not url"

    edited_outlet = await edit_existing_outlet([mock_newsoutlet_DTO])

    assert isinstance(edited_outlet, list)
    assert len(edited_outlet) == 0

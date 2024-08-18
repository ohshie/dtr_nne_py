import pytest

from business.outlet_manager.newsoutlet_manager import (
    get_current_outlets,
    add_new_outlet,
)
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.mocks.newsoutlet_mocks import mock_newsoutlet_DTO_list_factory
from tests.newsoutlet_tests.clear_newsoutlets_table import clear_newsoutlets_table


@pytest.mark.asyncio
async def test_get_newsoutlets_default():
    await clear_newsoutlets_table()
    await add_new_outlet(mock_newsoutlet_DTO_list_factory(2))

    current_outlets = await get_current_outlets()

    assert isinstance(current_outlets, list)
    assert len(current_outlets) == 2
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in current_outlets)


@pytest.mark.asyncio
async def test_get_newsoutlets_empty():
    await clear_newsoutlets_table()

    current_outlets = await get_current_outlets()

    assert current_outlets is None

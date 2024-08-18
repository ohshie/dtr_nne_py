import pytest

from business.outlet_manager.newsoutlet_manager import add_new_outlet
from models.dto.newsoutlet_dto import NewsOutletDTO
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_list_factory,
    mock_newsoutlet_DTO_factory,
)
from tests.newsoutlet_tests.clear_newsoutlets_table import clear_newsoutlets_table


@pytest.mark.asyncio
async def test_add_newsoutlet_func_base():
    await clear_newsoutlets_table()

    outlets_dto_list: list[NewsOutletDTO] = mock_newsoutlet_DTO_list_factory(2)

    outlets_DTO = await add_new_outlet(outlets_dto_list)

    assert isinstance(outlets_DTO, list)
    assert len(outlets_DTO) > 0
    assert all(isinstance(outlet, NewsOutletDTO) for outlet in outlets_DTO)


@pytest.mark.asyncio
async def test_add_newsoutlet_func_empty():
    await clear_newsoutlets_table()
    result = await add_new_outlet([])
    assert result == []


@pytest.mark.asyncio
async def test_add_newsoutlet_func_duplicate():
    await clear_newsoutlets_table()
    outlets_dto_list: list[NewsOutletDTO] = mock_newsoutlet_DTO_list_factory(2)
    outlets_dto_list.append(outlets_dto_list[0])

    result = await add_new_outlet(outlets_dto_list)

    assert len(outlets_dto_list) != len(result)


@pytest.mark.asyncio
async def test_add_newsoutlet_func_invalid():
    await clear_newsoutlets_table()
    result = await add_new_outlet([mock_newsoutlet_DTO_factory(correct=False)])

    assert result == []

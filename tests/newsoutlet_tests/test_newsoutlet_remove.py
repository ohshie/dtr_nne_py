import asyncio

import pytest

from business.outlet_manager.newsoutlet_manager import (
    add_new_outlet,
    remove_existing_outlet,
)
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_DTO_correct_1,
    mock_newsoutlet_DTO_correct_2,
    mock_newsoutlet_DTO_invalidurl,
)
from tests.newsoutlet_tests.clear_newsoutlets_table import clear_newsoutlets_table


@pytest.mark.asyncio
async def test_remove_newsoutlet_base():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2])

    removed_outlets = await remove_existing_outlet([mock_newsoutlet_DTO_correct_1])

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 1
    assert removed_outlets[0] == mock_newsoutlet_DTO_correct_1


@pytest.mark.asyncio
async def test_remove_newsoutlet_multiple():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2])

    removed_outlets = await remove_existing_outlet(
        [mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2]
    )

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 2


@pytest.mark.asyncio
async def test_remove_newsoutlet_empty():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1])

    removed_outlets = await remove_existing_outlet([])

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 0


@pytest.mark.asyncio
async def test_remove_newsoutlet_notfound():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1])

    removed_outlets = await remove_existing_outlet([mock_newsoutlet_DTO_correct_2])

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 0


@pytest.mark.asyncio
async def test_remove_newsoutlet_duplicate():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2])

    removed_outlets = await remove_existing_outlet(
        [mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_1]
    )

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 1
    assert removed_outlets[0] == mock_newsoutlet_DTO_correct_1


@pytest.mark.asyncio
async def test_remove_newsoutlet_partial():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1])

    removed_outlets = await remove_existing_outlet(
        [mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2]
    )

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 1
    assert removed_outlets[0] == mock_newsoutlet_DTO_correct_1


@pytest.mark.asyncio
async def test_remove_newsoutlet_invalid():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1])

    removed_outlets = await remove_existing_outlet([mock_newsoutlet_DTO_invalidurl])

    assert isinstance(removed_outlets, list)
    assert len(removed_outlets) == 0


@pytest.mark.asyncio
async def test_remove_newsoutlet_concurrency():
    await clear_newsoutlets_table()
    await add_new_outlet([mock_newsoutlet_DTO_correct_1, mock_newsoutlet_DTO_correct_2])

    removal_tasks = [
        remove_existing_outlet([mock_newsoutlet_DTO_correct_1]),
        remove_existing_outlet([mock_newsoutlet_DTO_correct_2]),
    ]

    results = await asyncio.gather(*removal_tasks)

    for result in results:
        assert isinstance(result, list)
        assert len(result) == 1

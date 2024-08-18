from fastapi import APIRouter, Response, status

from business.outlet_manager.newsoutlet_manager import (
    get_current_outlets,
    add_new_outlet,
    edit_existing_outlet,
    remove_existing_outlet,
)
from models.dto.newsoutlet_dto import NewsOutletDTO

router = APIRouter()


@router.get("/GetCurrentOutlets", response_model=list[NewsOutletDTO])
async def get_current_outlets_controller(response: Response):
    current_outlets = await get_current_outlets()

    if not current_outlets:
        response.status_code = status.HTTP_204_NO_CONTENT
        return []

    return current_outlets


@router.post("/AddNewOutlet", status_code=201, response_model=list[NewsOutletDTO])
async def add_news_outlet_controller(
    newsoutlets: list[NewsOutletDTO], response: Response
) -> list[NewsOutletDTO]:
    added_outlets = await add_new_outlet(newsoutlets)

    if len(added_outlets) == 0:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return added_outlets


@router.put("/UpdateNewsOutlet", response_model=list[NewsOutletDTO])
async def update_news_outlet_controller(
    newsoutlets: list[NewsOutletDTO], response: Response
):
    updated_outlets = await edit_existing_outlet(newsoutlets)

    if len(updated_outlets) == 0:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return updated_outlets


@router.delete("/DeleteNewsOutlet", response_model=list[NewsOutletDTO])
async def delete_news_outlet_controller(
    newsoutlets: list[NewsOutletDTO], response: Response
):
    deleted_outlets = await remove_existing_outlet(newsoutlets)

    if len(deleted_outlets) == 0:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return deleted_outlets

from fastapi import APIRouter
from models.dto.newsoutlet_dto import NewsOutletDTO

router = APIRouter()

@router.post("/AddNewOutlet", status_code=201, response_model=list[NewsOutletDTO])
async def add_new_outlet(newsoutlet: list[NewsOutletDTO]) -> list[NewsOutletDTO]:
    added_outlets = newsoutlet

    return added_outlets
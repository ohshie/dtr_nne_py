from datalayer.repositories.newsoutlet_repository import NewsOutletRepository
from datalayer.unitofwork.unit_of_work import UnitOfWork


async def clear_newsoutlets_table():
    async with UnitOfWork() as uow:
        newsoutlet_repository = NewsOutletRepository(uow)
        await newsoutlet_repository.clear_table()
        await uow.commit()

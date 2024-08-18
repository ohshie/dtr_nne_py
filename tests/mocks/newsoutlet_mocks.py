from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO

test_outlets_DTO: list[NewsOutletDTO] = [
    NewsOutletDTO(
        inUse=True,
        alwaysJs=False,
        name="first_outlet",
        website="http://website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
    NewsOutletDTO(
        inUse=True,
        alwaysJs=False,
        name="second_outlet",
        website="http://website2.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
]

test_outlets: list[NewsOutlet] = [
    NewsOutlet(
        id=1,
        inUse=True,
        alwaysJs=False,
        name="first_outlet",
        website="website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
    NewsOutlet(
        id=2,
        inUse=True,
        alwaysJs=False,
        name="second_outlet",
        website="website.url",
        mainPageCss="random",
        newsPageCss="random",
    ),
]

from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO
from faker import Faker


def mock_newsoutlet_DTO_factory(correct: bool = True) -> NewsOutletDTO:
    fake = Faker()

    newsoutlet_dto = NewsOutletDTO(
        name=fake.name(),
        website=fake.url(),
        newsPageCss=fake.json(num_rows=2),
        mainPageCss=fake.json(num_rows=2),
        inUse=fake.boolean(),
        alwaysJs=fake.boolean(),
    )
    if not correct:
        newsoutlet_dto.website = fake.state()

    return newsoutlet_dto


def mock_newsoutlet_DTO_list_factory(
    num: int, correct: bool = True
) -> list[NewsOutletDTO]:
    newsoutlet_dto_list: list[NewsOutletDTO] = []
    for num in range(num):
        newsoutlet_dto_list.append(mock_newsoutlet_DTO_factory(correct))

    return newsoutlet_dto_list


def mock_newsoutlet_factory(correct: bool = True) -> NewsOutlet:
    fake = Faker()
    newsoutlet = NewsOutlet(
        name=fake.name(),
        website=fake.url(),
        newsPageCss=fake.json(num_rows=2),
        mainPageCss=fake.json(num_rows=2),
        inUse=fake.boolean(),
        alwaysJs=fake.boolean(),
    )

    if not correct:
        newsoutlet.website = fake.state()

    return newsoutlet


def mock_newsoutlet_list_factory(num: int, correct: bool = True) -> list[NewsOutlet]:
    newsoutlet_list: list[NewsOutlet] = []
    for num in range(num):
        newsoutlet_list.append(mock_newsoutlet_factory(correct))

    return newsoutlet_list


mock_newsoutlet_emptyname = NewsOutlet(
    name="",
    website="http://test.org",
    newsPageCss="test",
    mainPageCss="test",
    inUse=False,
    alwaysJs=False,
)

mock_newsoutlet_invalidurl = NewsOutlet(
    name="test",
    website="test.org",
    newsPageCss="test",
    mainPageCss="test",
    inUse=False,
    alwaysJs=False,
)

mock_newsoutlet_emptymainpagecss = NewsOutlet(
    name="test",
    website="test.org",
    newsPageCss="test",
    mainPageCss="",
    inUse=False,
    alwaysJs=False,
)

mock_newsoutlet_emptynewspagecss = NewsOutlet(
    name="test",
    website="test.org",
    newsPageCss="",
    mainPageCss="test",
    inUse=False,
    alwaysJs=False,
)

from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO

mock_newsoutlet_DTO_correct_1 = NewsOutletDTO(
    name="test",
    website="http://test.org",
    newsPageCss="test",
    mainPageCss="test",
    inUse=True,
    alwaysJs=False,
)

mock_newsoutlet_DTO_correct_2 = NewsOutletDTO(
    name="test",
    website="http://test_2.org",
    newsPageCss="test",
    mainPageCss="test",
    inUse=True,
    alwaysJs=False,
)

mock_newsoutlet_DTO_invalidurl = NewsOutletDTO(
    name="test",
    website="test.org",
    newsPageCss="",
    mainPageCss="test",
    inUse=False,
    alwaysJs=False,
)

mock_newsoutlet_correct_1 = NewsOutlet(
    name="test",
    website="http://test.org",
    newsPageCss="test",
    mainPageCss="test",
    inUse=True,
    alwaysJs=False,
)

mock_newsoutlet_correct_2 = NewsOutlet(
    name="test",
    website="http://test_2.org",
    newsPageCss="test",
    mainPageCss="test",
    inUse=True,
    alwaysJs=False,
)

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

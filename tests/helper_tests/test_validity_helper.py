from helpers.validity_helper import is_valid_str_field, is_valid_outlet_object
from models.domainmodels.newsoutlet import NewsOutlet

mock_newsoutlet_correct = NewsOutlet(
    name="test",
    website="http://test.org",
    newsPageCss="test",
    mainPageCss="test",
)

mock_newsoutlet_emptyname = NewsOutlet(
    name="",
    website="http://test.org",
    newsPageCss="test",
    mainPageCss="test",
)

mock_newsoutlet_invalidurl = NewsOutlet(
    name="test",
    website="test.org",
    newsPageCss="test",
    mainPageCss="test",
)

mock_newsoutlet_emptymainpagecss = NewsOutlet(
    name="test",
    website="test.org",
    newsPageCss="test",
    mainPageCss="",
)

mock_newsoutlet_emptynewspagecss = NewsOutlet(
    name="test",
    website="test.org",
    newsPageCss="",
    mainPageCss="test",
)


def test_is_valid_str_field():
    assert is_valid_str_field("a") == True
    assert is_valid_str_field("123") == True
    assert is_valid_str_field(" a ") == True

    assert is_valid_str_field(" ") == False
    assert is_valid_str_field("") == False
    assert is_valid_str_field(None) == False
    assert is_valid_str_field(123) == False


def test_is_valid_outlet_object():
    assert is_valid_outlet_object(mock_newsoutlet_correct) == True
    assert is_valid_outlet_object(mock_newsoutlet_emptyname) == False
    assert is_valid_outlet_object(mock_newsoutlet_invalidurl) == False
    assert is_valid_outlet_object(mock_newsoutlet_emptymainpagecss) == False
    assert is_valid_outlet_object(mock_newsoutlet_emptynewspagecss) == False

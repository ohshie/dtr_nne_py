from helpers.validity_helper import is_valid_str_field, is_valid_outlet_object
from tests.mocks.newsoutlet_mocks import (
    mock_newsoutlet_correct_1,
    mock_newsoutlet_invalidurl,
    mock_newsoutlet_emptyname,
    mock_newsoutlet_emptymainpagecss,
    mock_newsoutlet_emptynewspagecss,
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
    assert is_valid_outlet_object(mock_newsoutlet_correct_1) == True
    assert is_valid_outlet_object(mock_newsoutlet_emptyname) == False
    assert is_valid_outlet_object(mock_newsoutlet_invalidurl) == False
    assert is_valid_outlet_object(mock_newsoutlet_emptymainpagecss) == False
    assert is_valid_outlet_object(mock_newsoutlet_emptynewspagecss) == False

import pytest

from helpers.duplicates_helper import filter_duplicates, find_uniques


class RandomObject:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, RandomObject) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


def test_filter_duplicates_with_integers():
    assert filter_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
    assert filter_duplicates([5, 5, 5, 5]) == [5]


def test_find_duplicates_with_integers():
    assert find_uniques([1, 2, 2], [3, 4, 4]) == [3, 4]
    assert find_uniques([5, 5], [5, 5]) == []
    assert find_uniques([1, 2], [3]) == [3]


def test_filter_duplicates_with_strings():
    assert filter_duplicates(["abc", "bcd", "cde", "cde", "bcd"]) == [
        "abc",
        "bcd",
        "cde",
    ]
    assert filter_duplicates(["abc", "bcd", "cde"]) == ["abc", "bcd", "cde"]


def test_find_duplicates_with_strings():
    assert find_uniques(["abc", "bcd"], ["cde"]) == ["cde"]
    assert find_uniques(["abc", "abc"], ["abc", "abc"]) == []
    assert find_uniques(["abc", "bcd", "cde"], ["cde", "deg", "deg"]) == [
        "deg",
    ]


def test_filter_duplicates_with_custom_objects():
    obj1 = RandomObject(1)
    obj2 = RandomObject(2)
    obj3 = RandomObject(1)

    assert filter_duplicates([obj1, obj2, obj3]) == [obj1, obj2]
    assert filter_duplicates([obj1, obj1, obj1]) == [obj1]


def test_find_duplicates_with_custom_objects():
    obj1 = RandomObject(1)
    obj2 = RandomObject(2)
    obj3 = RandomObject(1)

    assert find_uniques([obj1, obj2], [obj3]) == []
    assert find_uniques([obj1, obj1, obj1], [obj3, obj2, obj1]) == [obj2]
    assert find_uniques([obj2, obj3], [obj1, obj3]) == []


def test_filter_duplicates_with_empty_list():
    assert filter_duplicates([]) == []


def test_find_duplicates_with_empty_list():
    assert find_uniques([], []) == []


def test_filter_duplicates_with_one_item():
    assert filter_duplicates([1]) == [1]
    assert filter_duplicates(["a"]) == ["a"]


def test_find_duplicates_with_one_item():
    assert find_uniques([1], [1]) == []
    assert find_uniques(["a"], ["a"]) == []

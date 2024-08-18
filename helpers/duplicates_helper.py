from typing import TypeVar, Generic

T = TypeVar("T")


def filter_duplicates(incomming_list: list[Generic[T]]) -> list[Generic[T]]:
    seen = set()
    outgoing_list = []
    for item in incomming_list:
        if item not in seen:
            outgoing_list.append(item)
            seen.add(item)

    return outgoing_list


def find_uniques(
    current_list: list[Generic[T]], incoming_list: list[Generic[T]]
) -> list[Generic[T]]:
    """
    receive 2 lists: list_1 and list_2
    check if list_1 contains values that are inside of list_2
    if it does - remove them from list_2
    """
    set_1 = set(current_list)
    set_2 = set(incoming_list)

    ougoing_list = [item for item in set_2 if item not in set_1]
    return ougoing_list


def find_similar(current_list: list[T], incoming_list: list[T]) -> list[T]:
    """
    :param current_list: Current list
    :param incoming_list: Received list
    :return: only values that are similar to received list
    """
    set_1 = set(current_list)
    set_2 = set(incoming_list)

    outgoing_list = [item for item in set_1 if item in set_2]
    return outgoing_list

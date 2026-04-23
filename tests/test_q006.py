from questions.q006_merge_two_sorted_lists import (
    merge_two_lists,
    build_linked_list,
    linked_list_to_list
)


def test_basic():
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])

    result = merge_two_lists(l1, l2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]


def test_empty_one():
    l1 = build_linked_list([])
    l2 = build_linked_list([0])

    result = merge_two_lists(l1, l2)
    assert linked_list_to_list(result) == [0]


def test_both_empty():
    result = merge_two_lists(None, None)
    assert result is None
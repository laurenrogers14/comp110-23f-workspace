"""Test my zip function."""

__author__ = "730711512"

from lessons.zip import zip


def test_non_empty_lists():
    """Checks to see if the lists in the function returns a dictionary."""
    list1 = []
    list2 = []
    result = zip(list1, list2)
    assert result == {}


def test_empty_lists():
    """Check to see that empty lists, return empty dictionaries."""
    list1 = ["Monday", "Tuesday"]
    list2 = [1, 2]
    result = zip(list1, list2)
    expected_result = {"Monday": 1, "Tuesday": 2}
    assert result == expected_result


def test_lists_of_dif_lengths():
    """Check to see if lists of different lengths still return empty dictionaries."""
    list1 = ["Apple", "Banana", "Orange"]
    list2 = [1, 2, 3]
    result_dict: dict[str, int] = zip(list1, list2)
    assert result_dict == {}
    
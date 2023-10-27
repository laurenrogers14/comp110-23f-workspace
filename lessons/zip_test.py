"""Test my zip function."""

__author__ = "730711512"


from lessons.zip import zip


def test_return_dict():
    """Checks to see if the lists in the function returns a dictionary"""
    assert zip([]) == dict[str, int]


def test_empty_str():
    """Check to see that empty lists, return empty dictionaries"""
    result_dict: dict[str, int] ={}
    assert zip(result_dict) == {}


def test_lists_of_dif_lengths():
    """Check to see if lists of different lengths still return dictionaries"""
    result_dict: dict[str, int] = {"Monday": 1, "Tuesday": 2}
    assert zip(result_dict) == dict[str, int]
    
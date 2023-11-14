"""Writing Unit Test for Dictionary Funcions."""

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


__author__ = "730711512"


def test_invert_use_case1():
    """This unit test returns a inverted dictionary of letters."""
    dict1 = {'a': 'z', 'b': 'y', 'c': 'x'}
    result = invert(dict1)
    assert result == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_case2():
    """This unit test returns a inverted dictionayr of words."""
    dict1 = {'apple': 'cat', 'orange': 'dog'}
    result = invert(dict1)
    assert result == {'cat': 'apple', 'dog': 'orange'}


def test_invert_edge_case():
    """This unit test raises a key error, because of the two keys are not unique."""
    dict1 = {'a': 'z', 'b': 'z'}
    with pytest.raises(KeyError):
        dict1 = {'a': 'z', 'b': 'z'}
        invert(dict1)


def test_favorite_color_use_case1():
    """This unit test returns the color that appears the most."""
    dict2 = {'jane': 'blue', 'lauren': 'yellow', 'isabel': 'blue'}
    result = favorite_color(dict2)
    assert result == 'blue'


def test_favorite_color_use_case2():
    """This unit tests returns the color that appears first, because there is a tie."""
    dict2 = {'jane': 'green', 'lauren': 'blue'}
    result = favorite_color(dict2)
    assert result == 'green'


def test_favorite_color_edge_case():
    """This unit test returns the color the appears the most frequently, even if it is not first."""
    dict2 = {'jane': 'blue', 'lauren': 'green', 'liam': 'green'}
    result = favorite_color(dict2)
    assert result == 'green'


def test_count_use_case1():
    """This unit test returns each key with a unique value."""
    input_list = {'a', 'b', 'a', 'c', 'b', 'b'}
    result = count(input_list)
    assert result == {'a': 1, 'b': 1, 'c': 1}


def test_count_use_case2():
    """This unit test returns each word with a unique value."""
    input_list = {'apple', 'banana', 'orange', 'banana'}
    result = count(input_list)
    assert result == {'apple': 1, 'banana': 1, 'orange': 1}


def test_count_edge_case():
    """This unit tests asserts that an empty input list will return an empty dictionary."""
    input_list = {}
    result = count(input_list)
    assert result == {}


def test_alphabetizer_use_case1():
    """This unit test asserts that each key is a letter and each value is a list of the words that begin with that letter."""
    input_list2 = ["cat", "apple", "boy", "angry", "bad", "car"]
    result = alphabetizer(input_list2)
    assert result == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    

def test_alphabetizer_use_case2():
    """This unit test asserts that each key is a unique letter and each value is a list of words tht begin with that letter."""
    input_list2 = ["dog", "elephant", "apple", "bee", "zebra"]
    result = alphabetizer(input_list2)
    assert result == {'d': ['dog'], 'e': ['elephant'], 'a': ['apple'], 'b': ['bee'], 'z': ['zebra']}


def test_alphabetizer_edge_case():
    """This unit tests asserts that an empty input list will return an empty dictionary."""
    input_list2 = []
    result = alphabetizer(input_list2)
    assert result == {}
    

def test_update_attendance_use_case1():
    """This function should update the new attendance information."""
    dict3 = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(dict3, "Tuesday", "Vrinda")
    assert dict3 == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_use_case2():
    """This function should update the new attendance information."""
    dict3 = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(dict3, "Wednesday", "John")
    assert dict3 == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['John']}


def test_update_attendance_edge_case():
    """This function should update the new attendance information even after beginning with an empty dictionary."""
    dict3 = {}
    update_attendance(dict3, "Tuesday", "Vrinda")
    assert dict3 == {'Tuesday': ['Vrinda']}
"""Writing Unit Test for Dictionary Funcions."""

__author__= "730711512"

from exercises.ex06.dictionary import invert

def test_invert_using_letters():
    input_dict = {'a': 'z', 'b': 'y', 'c': 'x'}
    result = invert(input_dict)
    assert result == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_using_words():
    input_dict = {'apple': 'cat', 'orange': 'dog'}
    result = invert(input_dict)
    assert result == {'cat': 'apple', 'dog': 'orange'}


def test_invert_with_keys_of_same_value():
    input_dict = {'a': 'z', 'b': 'z'}
    with input_dict.raises(KeyError):
        input_dict = {'a': 'z', 'b': 'z'}
        invert(input_dict)

from exercises.ex06.dictionary import favorite_color

def test_favorite_color_use_case1():
    input_dict = {'blue': 'jane', 'blue': 'lauren'}
    result = favorite_color(input_dict)
    assert result == 'blue'

def test_favorite_color_use_case2():
    input_dict = {'blue': 'jane', 'green': 'lauren'}
    result = favorite_color(input_dict)
    assert result == 'blue'

def test_favorite_color_edge_case():
    input_dict = {'blue': 'jane', 'green': 'lauren', 'green': 'liam'}
    result = favorite_color(input_dict)
    assert result == 'green'

from exercises.ex06.dictionary import count

def test_count_use_case1():
    input_dict = {'apple', 'banana', 'apple', 'banana'}
    result = count(input_dict)
    assert result == {'apple': 2, 'banana': 2}

def test_count_use_case2():
    input_dict = {'apple', 'banana', 'orange', 'banana'}
    result = count(input_dict)
    assert result == {'apple' : 1, 'banana': 2, 'orange': 1}

def test_count_edge_case():
    input_dict = {}
    result = count(input_dict)
    assert result == {}

from exercises.ex06.dictionary import alphabetizer

def test_alphabetizer_use_case1():
    input_dict = ["cat", "apple", "boy", "angry", "bad", "car"]
    result = alphabetizer(input_dict)
    assert result == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}

def test_alphabetizer_use_case2():
    input_dict = ["dog", "elephant", "apple", "bee", "zebra"]
    result = alphabetizer(input_dict)
    assert result == {'d': ['dog'], 'e': ['elephant'], 'a': ['apple'], 'b': ['bee'], 'z': ['zebra']}

def test_alphabetizer_edge_case():
    input_dict = []
    result = alphabetizer(input_dict)
    assert result == {}

from exercises.ex06.dictionary import update_attendance

def test_update_attendance():
    input_dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance[input_dict] = "Tuesday", "Vrinda"
    assert input_dict == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}

def test_update_attendance_use_case2():
    input_dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance[input_dict] = "Wednesday", "John"
    assert input_dict == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['John']}

def test_update_attendance_edge_case():
    input_dict = {}
    update_attendance[input_dict] = "Tuesday", "Vrinda"
    assert input_dict == {'Tuesday': ['Vrinda']}





"""EX04 - 'list' Utility Functions."""

__author__ = "730711512"


def all(input1: list[int], input2: int) -> bool:
    """Given a list see if it completely matches the given integer."""

    i: int = 0
    if len(input1) == 0:
        return False
    while len(input1) > i:
        if input1[i] != input2:
            return False  
        i = i + 1
    return True

def max(input3: list[int]) -> int: 
    """Given a list of integers, the function should return the largest one."""

    i: int = 0
    if len(input3) == 0:
        raise ValueError("max() arg is an empty List")
    max_number: int = input3[0]
    while len(input3) > i:
        if input3[i] > max_number:
            max_number = input3[i]
        i = i + 1
    return max_number

def is_equal(input5: list[int], input6: list[int]) -> bool:
    """Given two lists of integers, return True if every index in both lists are the same."""

    i: int = 0
    if len(input5) == 0:
        return False
    while len(input5) > i:
        if input5[i] != input6[i]:
            return False
        i = i + 1
    return True
    
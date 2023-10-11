"""EX04 - 'list' Utility Functions. """

__author__ = "730711512"


i: int = 0
def all(input1: list[int], input2: int) -> bool:
    """Given a list see if it completely matches the given integer. """
    if len(input1) == 0:
        raise ValueError("max() arg is an empty List")
    while len(input1) < input2:
        if input1[i] != input2:
            return False  
    i = i + 1
    return True
def max(input3: list[int]) -> int: 
    """Given a list of integers, the function should return the largest one. """
    if len(input3) == 0:
        raise ValueError("max() arg is an empty List")
    while len(input3) > i:
        if input3[i] > input3[i]:
            print(input3[i + 1])
    i = i + 1
    return True

def is_equal(input5: list[int], input6: list[int]) -> bool:
    """Given two lists of integers, return True if every index in both lists are the same."""
    while len(input5) <= len(input6):
        if(input5[i]) == input6[i]:
            return True
        i = i + 1
    return False
    
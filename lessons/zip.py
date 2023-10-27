"""Combing two lists into a dictionry"""

__author__ = "730711512"

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    result_dict: dict[str, int] = {}
    if len(list1) != len(list2):
        return {}
    if list1 == {}:
        return{}
    if list2 == {}:
        return{}

    for i in range(len(list1)):
        str_value = list1[i]
        int_value = list2[i]
        result_dict[str_value] = int_value
    
    return result_dict

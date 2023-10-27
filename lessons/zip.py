"""Combing two lists into a dictionry"""

__author__ = "730711512"

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    if len(list1) != len(list2):
        return {}
    if list1 == {}:
        return{}
    if list2 == {}:
        return{}

result_dict: dict[str, int] = {"mahomes": 15, "kelce": 87}
print(result_dict)
    

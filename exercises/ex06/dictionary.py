"""Working with Dictionary Functions."""

__author__ = "730711512"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}
    i: int = 0

    for key, value in dict1: 
        if value in inverted_dict:
            raise KeyError("Key values are unique and can only appear once!")
        inverted_dict[value] = key
    
    return inverted_dict




def favorite_colors(dict2: dict[str, str]) -> str: 
    color_count = {}
    most_pop_color = None
    max_count = 0

    for name, color in dict2:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count = 1
        
        if color_count[color] > max_count or (color_count[color] == max_count and dict2[color] == color):
            max_count = color_count[color]
            most_pop_color = color


def count(input_list: list[str]) -> dict[str, int]:
    result_dict = {}
    return_dict: dict[str, int]
    i: int = 0

    for elem in input_list:
        if input_list in return_dict:
            result_dict[elem] += 1
        else:
            result_dict[elem] = 1

    return result_dict

def alphabetizer(input_list2: list[str]) -> dict[str, list[str]]:
    result_dict2 = {}

    for elem in input_list2:
        elem = elem.lower()
        first_letter = elem[0]
    
        if first_letter in result_dict2:
            result_dict2[first_letter].append(elem)
        else:
            result_dict2[first_letter] = [elem]
        
    return result_dict2


def update_attendance(dict3: dict[str, list[str]], day_of_week: str, student: str):

    if day_of_week in dict3:
        dict3[day_of_week].append(student)
    else:
        dict3[day_of_week] = [student]
    
    return dict3









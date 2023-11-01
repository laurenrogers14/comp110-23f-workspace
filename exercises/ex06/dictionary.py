"""Working with Dictionary Functions."""

__author__ = "730711512"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """This function returns an inverted version of the orginal dictionary."""
    inverted_dict: dict[str, str] = {}

    for key in dict1: 
        value: str = dict1[key]
        if value in inverted_dict:
            raise KeyError(f"Duplicate key {value} encountered while inverting!")
        else:
            inverted_dict[value] = key
    
    return inverted_dict


def favorite_color(dict2: dict[str, str]) -> str: 
    """This function returns the most popular color in the dictionary."""
    color_count: dict[str, int] = {}
    most_pop_color: str = ""
    max_count = 0
   
    for key in dict2:
        value: str = dict2[key]
        if value in color_count:
            color_count[value] += 1
        else:
            color_count[value] = 1 
    for elem in color_count:
        if color_count[elem] > max_count:
            max_count = color_count[elem]
            most_pop_color = elem

    return most_pop_color


def count(input_list: list[str]) -> dict[str, int]:
    """This function returns a dictionary of the counts of each of the items in the input list."""
    result_dict: dict[str, int] = {}

    for elem in input_list:
        if elem in result_dict:
            result_dict[elem] += 1
        else:
            result_dict[elem] = 1

    return result_dict


def alphabetizer(input_list2: list[str]) -> dict[str, list[str]]:
    """This function returns a dictionary of the letters and the lists of words that belong to that letter."""
    result_dict2: dict[str, list[str]] = {}

    for elem in input_list2:
        elem = elem.lower()
        first_letter = elem[0]
    
        if first_letter in result_dict2:
            result_dict2[first_letter].append(elem)
        if first_letter not in result_dict2:
            result_dict2[first_letter] = [elem]
        
    return result_dict2


def update_attendance(dict3: dict[str, list[str]], day_of_week: str, student: str) -> dict[str, list[str]]:
    """This function should update the new attendance information."""
    if day_of_week in dict3:
        dict3[day_of_week].append(student)
    else:
        dict3[day_of_week] = [student]
    
    return dict3
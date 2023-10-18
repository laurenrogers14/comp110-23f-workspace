"""Summing the elements of a list using different loops."""
__author__ = "730711512"


def w_sum(vals: list[float]) -> float:
    """Given a list of decimals, return the sum using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals): 
        sum = sum + vals[idx]
        idx = idx + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Given a list of decimals, return the sum using for in loops."""
    sum: float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum 


def f_range_sum(vals: list[float]) -> float:
    """Given a list of decimals, return the sum using for in range loops."""
    idx: int = 0
    sum: float = 0.0 
    for idx in range(0, len(vals)):
        sum = sum + vals[idx]
    return sum

"""Practice with for loops"""

__author__ = "730711512"

w_sum: list[float] = 1.1, 0.9, 1.0

def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum = float(0.0)
    while idx < len(vals): 
        sum = vals[0]
        idx = idx + 1
    return sum


f_sum: list[float] = 1.1, 0.9, 1.0

def f_sum (vals: list[float]) -> float:
    sum = float(0.0)
    for elem in f_sum:
        print(elem[0])
        f_sum = f_sum + 1
    return sum 


f_range_sum: list[float] = 1.1, 0.9, 1.0

def f_range_sum (vals: list[float]) -> float:
    idx: int = 0
    sum = float (0.0)
    for idx in range(0, len(f_range_sum)):
        print(f_range_sum[0])
        f_range_sum = f_range_sum + 1
    return sum
        






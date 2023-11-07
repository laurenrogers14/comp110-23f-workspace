"""Intro to Object Oriented Programming."""

from __future__ import annotations

__author__ = "730711512"

class Point:

    x: float
    y: float 

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init


    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor

    
    def scale(self, factor:int) -> 'Point':
        return Point (self.x * factor, self.y * factor)

Point_1: Point = (2.0, 3.0)
Point_1.scale_by(4.0)
new_point: Point = Point_1.scale(3.0)
print(new_point.x)
print(new_point.y)
    


        

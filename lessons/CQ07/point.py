"""Intro to Object Oriented Programming."""

__author__ = "730711512"

from lessons.CQ07.point import Point

x: float
y: float

class Point:
    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init


    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor

    
    def scale(self, factor:int) -> 'Point':
        return Point (self.x * factor, self.y * factor)

        

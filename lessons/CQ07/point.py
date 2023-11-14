"""Intro to Object Oriented Programming."""
from __future__ import annotations

__author__ = "730711512"


class Point:
    """Creating a Point class."""

    x: float
    y: float 

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Creating a Point class that has both x and y attributes."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Writing a method that prints out points in a readable way."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Writing a method so that it creates a new Point where both x and y are multipled by factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Writing a method that creates a new Point, but adds to the x and u attributes."""
        return Point(self.x + factor, self.y + factor)

    def scale_by(self, factor: int) -> None:
        """Wriitng a method that belongs to the Point class and mutates a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Writing a method that belongs to the Point class and creates a new Point."""
        return Point(self.x * factor, self.y * factor)
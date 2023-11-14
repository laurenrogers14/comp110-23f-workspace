"""Calling methods."""

from lessons.CQ07.point import Point

Point_1: Point = (2.0, 3.0)
Point_1.scale_by(4.0)
new_point: Point = Point_1.scale(3.0)
print(new_point.x)
print(new_point.y)
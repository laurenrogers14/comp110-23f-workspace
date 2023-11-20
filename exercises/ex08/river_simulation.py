"""Implementing the __init__ method."""

from exercises.ex08.river import River

my_river = River(num_fish=10, num_bears=2)
print(my_river.one_river_day())
print(my_river.view_river())
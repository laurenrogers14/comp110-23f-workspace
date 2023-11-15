"""Implementing the __init__ method."""

from exercises.ex08.river import River

my_river = River(num_fish = 10, num_bears = 2)
my_river.view_river(0, 10, 2)

my_river = River()
my_river.one_river_week()


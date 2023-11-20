"""File to define Fish class."""


class Fish:
    """Working with classes."""

    age: int
    
    def __init__(self):
        """My constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """This method should increase the age attribute by 1."""
        self.age = self.age + 1
        return None
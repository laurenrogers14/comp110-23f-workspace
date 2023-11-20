"""File to define Bear class."""


class Bear:
    """Working with classes."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """My constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """This methoud should increase the age attribute by 1."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1
        return None

    def eat(self, num_fish: int):
        """This method should update the bear's hunger score."""
        self.hunger_score = self.hunger_score + num_fish
        return None
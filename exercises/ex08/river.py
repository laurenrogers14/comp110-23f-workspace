"""File to define River class."""
__author__ = "730711512"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Represents a river ecosystem."""

    day: int  # the int tells you what day of the river's lifecycle you are modeling
    bears: list  # the list of Bears that stores the river's bear population
    fish: list  # a list of Fish that stores the river's fish population
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This method should check the ages of the fish and bears."""
        new_fish = [fish for fish in self.fish if fish.age <= 3]
        self.fish = new_fish

        # Remove bears older than 5
        new_bears = [bear for bear in self.bears if bear.age <= 5]
        self.bears = new_bears
    
    def remove_fish(self, amount: int):
        """This method should remove amount many Fish from the River."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """This method should remove the fish that the bear eats."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """This method should check the hunger score of every bear."""
        for bear in self.bears:
            if bear.hunger_score >= 0:
                self.bears.remove(bear)
        return None
        
    def repopulate_fish(self):
        """This method should declare that each pair of fish will produce 4 offspring."""
        new_fish = [Fish() for _ in range((len(self.fish) // 2) * 4)]
        self.fish.extend(new_fish)
        return None
    
    def repopulate_bears(self):
        """This method should declare that each pair of Bear's will produce 1 offspring."""
        new_bears = [Bear() for _ in range(len(self.bears) // 2)]
        self.bears.extend(new_bears)
        return None
    
    def view_river(self):
        """This method should print the day, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        for _ in range(7):
            # Simulate one day for all Bears
            for bear in self.bears:
                bear.one_day()
            # Simulate one day for all Fish
            for fish in self.fish:
                fish.one_day()
            # Simulate Bear's eating
            self.bears_eating()
            # Remove hungry Bear's from River
            self.check_hunger()
            # Remove old Fish and Bear's from River
            self.check_ages()
            # Simulate Fish repopulation
            self.repopulate_fish()
            # Simulate Bear repopulation
            self.repopulate_bears()
        # Visualize River
        self.view_river()
        # Increase day by 1
        self.day += 1
            
    def one_river_week(self):
        """This method should call the one_day() seven times."""
        for _ in range(7):
            self.one_river_day()

"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:

    day: int # the int tells you what day of the river's lifecycle you are modeling
    bears: list # the list of Bears that stores the river's bear population
    fish: list # a list of Fish that stores the river's fish population
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_list: list[Bear] = []
        if Fish > 3:
            self.fish.pop(Fish())
        if Bear > 5:
            self.bears.pop(Bear())
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat()
        return None
    
    def check_hunger(self):
        for bear in self.bears:
            if bear.hunger_score[bear] > 0:
                River.pop(bear)
        return None
        
    def repopulate_fish(self):
        new_fish:[Fish() = for _ in range(len(self.fish)) //2 * 4]
        self.fish.extend(new_fish)
        return None
    
    def repopulate_bears(self):
        new_bears: [Bear() = for _ in range(len(self.bears)) //2]
        self.bears.extend(new_bears)
        return None
    
    def view_river(self):
        print(f"Day: {self.day} ")
        print(f"Fish Population: {self.fish}")
        print(f"Bear Population: {self.bears}")
        
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
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
            
def one_river_week(self):
    for _ in range(7):
        self.one_river_day()
    return None

def remove_fish(self, amount: int):
    self.fish = self.fish[amount: ]
    Fish.pop(amount)

    return None
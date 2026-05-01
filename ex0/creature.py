from abc import ABC, abstractmethod


class creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def atack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Pokemon):
    def __init__(self):
        super().__init__("flameling", "fire")
    
    def atack(self):
        return f"{self.name} used Ember!"


class Pyrodon(Pokemon):
    def __init__(self):
        super().__init__("Pyrodon", "fire")

    def atack(self):
        return f"{self.name} used fire Flamethrower!"


class Aquanub(Pokemon):
    def __init__(self):
        super().__init__("Aquanub", "water")

    def atack(self):
        return f"{self.name} used water gun!"


class Torragon(Pokemon):
    def __init__(self):
        super().__init__("Torragon", "water")

    def atack(self):
        return f"{self.name} used bubble beam!"
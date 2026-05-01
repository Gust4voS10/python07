from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def atack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.type} type pokemon"


class chamander(Pokemon):
    def __init__(self):
        super().__init__("charmander", "fire")
    
    def atack(self):
        return f"{self.name} used flamethrower!"


class ponyta(Pokemon):
    def __init__(self):
        super().__init__("ponyta", "fire")

    def atack(self):
        return f"{self.name} used fire blast!"


class squirtle(Pokemon):
    def __init__(self):
        super().__init__("squirtle", "water")

    def atack(self):
        return f"{self.name} used water gun!"


class poliwag(Pokemon):
    def __init__(self):
        super().__init__("poliwag", "water")

    def atack(self):
        return f"{self.name} used bubble beam!"
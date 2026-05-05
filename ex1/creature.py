from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Creature) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Creature) -> str:
        return (f"{self.name} heals itself and {target} for large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        self.transformed = False
        super().__init__("Shiftling", "Normal")

    def attack(self):
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        self.transformed = False
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self):
        if self.transformed:
            return f"{self.name}  unleashes a devastating strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form."

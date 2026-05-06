from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1 import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        creature
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if (isinstance(creature, TransformCapability)):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if (self.is_valid(creature)):
            creat_copy = cast(TransformCapability, creature)
            print(creat_copy.transform())
            print(creature.attack())
            print(creat_copy.revert())
        else:
            raise ValueError(f"Invalid Creature '{creature.name}' "
                             f"for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if (isinstance(creature, HealCapability)):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if (self.is_valid(creature)):
            creat_copy = cast(HealCapability, creature)
            print(creature.attack())
            print(creat_copy.heal())
        else:
            raise ValueError(f"Invalid Creature {creature.name} "
                             "for this defensive strategy")

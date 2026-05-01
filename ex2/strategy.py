from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1 import HealCapability, TransformCapability
from typing import cast



class BattleStrategy:
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...
    
    @abstractmethod
    def act(self, creature: Creature, target: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self, creature: Creature, target: Creature) -> None:
        target
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature):
        if (isinstance(creature, TransformCapability)):
            return True
        return False
    
    def act(self, creature, target):
        if(self.is_valid(creature)):
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
    
    def act(self, creature: Creature, target: Creature) -> None:
        if (self.is_valid(creature)):
            creat_copy = cast(HealCapability, creature)
            print(creature.attack())
            print(creat_copy.heal(creature))
        else:
            raise ValueError(f"Invalid Creature {creature.name} "
                             "for this defensive strategy")
from abc import abstractmethod
from ex0.factory import Creature


class HealCapability:
    @abstractmethod
    def heal(self, target: Creature) -> str:
        ...


class TransformCapability:
    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
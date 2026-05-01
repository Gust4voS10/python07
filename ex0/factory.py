from abc import ABC, abstractmethod
from ex0.creature import creature, Flameling, Pyrodon, Aquanub, Torragon

class create_factory(ABC):
    @abstractmethod
    def create_base(self) -> creature:
        pass

    @abstractmethod
    def create_evolved(self) -> creature:
        pass
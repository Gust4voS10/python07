from abc import abstractmethod


class HealCapability:
    @abstractmethod
    def heal(self, target: str) -> str:
        ...


class TransformCapability:
    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...

from typing import Self, Protocol
from abc import abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class ValueObject[Type](Protocol):
    object: Type

    @abstractmethod
    def validate(self: Self) -> None:
        pass

    def __post__init__(self: Self) -> None:
        self.validate()
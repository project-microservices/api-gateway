from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, TypeVar, Protocol, Self

ValueT = TypeVar("ValueT", bound=Any)


@dataclass(frozen=True)
class ValueObject(Protocol):
    def __post_init__(self: Self) -> None:
        self.validate()

    @abstractmethod
    def validate(self: Self) -> None:
        pass
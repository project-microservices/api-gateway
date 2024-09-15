from typing import Generic, TypeVar
from dataclasses import dataclass

from src.app.domain.common.values_objects import ValueObject

DomainEntityBody = TypeVar("DomainEntityPath", bound=ValueObject)


@dataclass(frozen=True)
class DomainEntity(Generic[DomainEntityBody]):
    Body: DomainEntityBody
from typing import Generic, TypeVar
from dataclasses import dataclass

from src.app.domain.common.values_objects import ValueObject

DomainEntityId = TypeVar("DomainEntityPath", bound=ValueObject)


@dataclass(frozen=True)
class DomainEntity(Generic[DomainEntityId]):
    id: DomainEntityId
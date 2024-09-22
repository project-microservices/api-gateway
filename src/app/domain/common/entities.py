from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject

@dataclass
class BaseEntity[Type: ValueObject]:
    id: Type
from typing import Dict, Any, Optional, Self
from dataclasses import dataclass

from src.app.domain.common.exceptions import DomainValidationError
from src.app.domain.common.values_objects import ValueObject

        
        
@dataclass(frozen=True)
class Stream(ValueObject):
    stream: str

    def validate(self: Self) -> None:
        if not self.stream:
            raise DomainValidationError('stream must be str, not None')
        if not isinstance(self.stream, str):
            raise DomainValidationError('stream must be str')
        
@dataclass(frozen=True)
class UUID(ValueObject):
    uuid: str

    def validate(self: Self) -> None:
        if not self.uuid:
            raise DomainValidationError('uuid must be str, not None')
        if not isinstance(self.uuid, str):
            raise DomainValidationError('uuid must be str')
        
@dataclass(frozen=True)
class Body(ValueObject):
    body: Optional[Dict[Any, Any]] = None

    def validate(self: Self) -> None:
        if self.body!=None and not isinstance(self.body, dict):
           raise DomainValidationError(f'body must be dict or None')

@dataclass(frozen=True)
class Headers:
    headers: Optional[Dict[Any, Any]] = None

    def validate(self: Self) -> None:
        if self.headers!=None and not isinstance(self.headers, dict):
            raise DomainValidationError('headers must be dict or None')
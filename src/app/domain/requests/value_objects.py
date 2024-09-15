from typing import Dict, Any, Optional, Self
from dataclasses import dataclass

from src.app.domain.common.exceptions import DomainValidationError
from src.app.domain.common.values_objects import ValueObject


@dataclass(frozen=True)
class Method(ValueObject):
    method: str

    def validate(self: Self) -> None:
        if not self.method:
            raise DomainValidationError('method must be str, not None')
        if not isinstance(self.method, str):
            raise DomainValidationError('method must be str')
        if self.method not in ['POST', 'GET', 'DELETE', 'PUT']:
            raise DomainValidationError('Method not allowed')
        
@dataclass(frozen=True)
class Path(ValueObject):
    path: str

    def validate(self: Self) -> None:
        if not self.path:
            raise DomainValidationError('path must be str, not None')
        if not isinstance(self.path, str):
            raise DomainValidationError('path must be str')
        
@dataclass(frozen=True)
class Params(ValueObject):
    params: Dict[str, Any]

    def validate(self: Self) -> None:
        if not self.params:
            raise DomainValidationError('params must be dict, not None')
        if not isinstance(self.params, dict):
            raise DomainValidationError('params must be dict')
        
@dataclass(frozen=True)
class Body(ValueObject):
    body: Dict[Any, Any] = None

    def validate(self: Self) -> None:
       if not isinstance(self.body, dict) or not isinstance(self.body, None):
           raise DomainValidationError('body must be dict or None')

@dataclass(frozen=True)
class Headers:
    headers: Optional[Dict[str, Any]] = None

    def validate(self: Self) -> None:
        if not isinstance(self.headers, dict) or not isinstance(self.headers, None):
            raise DomainValidationError('headers must be dict or None')
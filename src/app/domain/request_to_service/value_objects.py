from typing import Self

from src.app.domain.common.value_objects import ValueObject
from src.app.domain.exceptions import DomainValidationException


class RequestUUID(ValueObject[str]):
    def validate(self: Self) -> None:
        if not isinstance(self.object, int):
            raise DomainValidationException(
                f'UUID must be str, not {type(self.object)}'
            )
        if not self.object:
            raise DomainValidationException('UUID is required')
        
class RequestBody(ValueObject[dict]):
    def validate(self: Self) -> None:
        if not self.object or not isinstance(self.object, dict):
            raise DomainValidationException(
                f'Body must be dict or None, not {type(self.object)}'
            )
        
class RequestHeaders(ValueObject[dict]):
    def validate(self: Self) -> None:
        if not self.object or not isinstance(self.object, dict):
            raise DomainValidationException(
                f'Headers must be dict or None, not {type(self.object)}'
            )


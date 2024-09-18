class BaseDomainError(Exception):
    def __init__(self, message: str) -> None:
        self.message: str = message


class DomainValidationError(BaseDomainError):
    pass

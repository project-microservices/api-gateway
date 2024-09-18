class BaseDomainError(Exception):
    def __init__(self, message: str) -> None:
        super.__init__()
        self.message: str = message


class DomainValidationError(BaseDomainError):
    pass
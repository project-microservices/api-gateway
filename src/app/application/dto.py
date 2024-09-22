from dataclasses import dataclass

@dataclass(frozen=True)
class RequestDTO:
    body: dict[str]
    headers: dict[str]


@dataclass(frozen=True)
class ResponseDTO:
    body: dict[str]
    status: int
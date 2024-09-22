from typing import Protocol, Self
from abc import abstractmethod

from app.domain.entity import RequestEntity


class RequestInterface(Protocol):
    @abstractmethod
    async def make_request(self: Self, request: RequestEntity) -> dict[str]:
        raise NotImplementedError
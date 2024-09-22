from typing import Protocol, Self
from abc import abstractmethod

from src.app.domain.request_to_service.entity import RequestEntity


class RequestInterface(Protocol):
    @abstractmethod
    async def make_request(self: Self, request: RequestEntity) -> dict[str]:
        raise NotImplementedError
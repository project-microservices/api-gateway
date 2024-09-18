from typing import Protocol, Self, Dict, Any
from abc import abstractmethod

from src.app.domain.requests.entities import RequestEntity


class RequestsRepository(Protocol):
    @abstractmethod
    async def make_request(self: Self, request: RequestEntity) -> Dict[Any, Any]:
        raise NotImplementedError
from typing import Generic, Protocol, TypeVar, Self

Request = TypeVar('Req')
Response = TypeVar('Res')


class Interactor(Generic[Request, Response], Protocol):
    async def __call__(self: Self, request: Request) -> Response:
        raise NotImplementedError

from typing import Protocol, Self

class Interactor[InputDTO, OutputDTO](Protocol):
    async def __call__(self: Self, request: InputDTO) -> OutputDTO:
        raise NotImplementedError
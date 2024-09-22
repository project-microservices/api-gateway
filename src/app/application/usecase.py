from typing import Self

from src.app.application.interactor import Interactor
from src.app.application.dto import RequestDTO, ResponseDTO
from src.app.domain.request_to_service.interfaces import RequestInterface

class MakeRequestToService(Interactor[RequestDTO, ResponseDTO]):
    def __init__(self: Self, request_interface: RequestInterface) -> None:
        self.request_interface: RequestInterface = request_interface

    async def __call__(self: Self, request: RequestDTO) -> ResponseDTO:
        pass
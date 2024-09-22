from typing import Self
from uuid import uuid4

from src.app.application.interactor import Interactor
from src.app.application.dto import RequestDTO, ResponseDTO
from app.domain.interfaces import RequestInterface
from app.domain.entity import RequestEntity
from app.domain.common.value_objects import RequestUUID, SendTo, RequestBody, RequestHeaders

class MakeRequestToService(Interactor[RequestDTO, ResponseDTO]):
    def __init__(self: Self, request_interface: RequestInterface) -> None:
        self.request_interface: RequestInterface = request_interface

    async def __call__(self: Self, request: RequestDTO) -> ResponseDTO:
        request_to_service = await self.request_interface.make_request(
            request = RequestEntity(
                uuid=RequestUUID(object=str(uuid4)),
                body=RequestBody(object=request.body),
                headers=RequestHeaders(object=request.headers),
                send_to=SendTo(object=request.send_to)
            )
        )
        return ResponseDTO(
            body=request_to_service.body,
            status=request_to_service.status
        )
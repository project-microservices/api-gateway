from typing import Self, Dict, Any
from uuid import uuid4

from src.app.domain.requests.entities import RequestEntity
from src.app.application.contracts.requests.requests import RequestToService
from src.app.application.contracts.requests.responses import ServiceResponse
from src.app.application.protocols.interactor import Interactor
from src.app.domain.requests.repositories import RequestsRepository
from src.app.domain.requests.value_objects import Body, Headers,  Stream, UUID


class MakeRequestToService(Interactor[RequestToService, ServiceResponse]):
    def __init__(self: Self, request_repository: RequestsRepository) -> None:
        self.request_repository: RequestsRepository = request_repository

    async def __call__(self: Self, request: RequestToService) -> ServiceResponse:
        uuid = str(uuid4)
        response: Dict[Any, Any] = await self.request_repository.make_request(
            request=RequestEntity(
                id=UUID(uuid),
                send_to=Stream(request.send_to),
                headers=Headers(request.headers),
                body=Body(request.body)
            )
        )

        return ServiceResponse(
            body=response
        )
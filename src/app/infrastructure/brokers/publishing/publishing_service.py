from typing import Self, Dict, Any
from faststream.nats import NatsBroker, NatsMessage

from src.app.domain.requests.entities import RequestEntity
from src.app.domain.requests.repositories import RequestsRepository


class PublishToService(RequestsRepository):
    def __init__(self: Self, broker: NatsBroker) -> None:
        self.broker: NatsBroker = broker

    async def make_request(self: Self, request: RequestEntity) -> Dict[Any, Any]:
        async with self.broker as broker:
            request_to_service: NatsMessage = await broker.publish(
                # correlation_id=request.id,
                rpc=True, 
                subject=request.send_to, 
                headers={},
                message=request.body,
                rpc_timeout=3.5
            )
        return request_to_service.body
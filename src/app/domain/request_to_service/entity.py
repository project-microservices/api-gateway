from dataclasses import dataclass

from src.app.domain.common.entities import BaseEntity
from src.app.domain.request_to_service.value_objects import RequestUUID, RequestBody, RequestHeaders


@dataclass
class RequestEntity(BaseEntity[RequestUUID]):
    uuid: RequestUUID
    body: RequestBody
    headers: RequestHeaders

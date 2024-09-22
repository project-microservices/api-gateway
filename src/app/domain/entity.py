from dataclasses import dataclass

from src.app.domain.common.entities import BaseEntity
from app.domain.value_objects import RequestUUID, RequestBody, RequestHeaders, SendTo


@dataclass
class RequestEntity(BaseEntity[RequestUUID]):
    uuid: RequestUUID
    body: RequestBody
    headers: RequestHeaders
    send_to: SendTo

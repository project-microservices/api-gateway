from typing import Dict, Any, Optional
from dataclasses import dataclass

from src.app.domain.common.entities import DomainEntity
from src.app.domain.requests.value_objects import Body, Headers, Stream, UUID


@dataclass(frozen=True)
class RequestEntity(DomainEntity[UUID]):
    id: UUID
    send_to: Stream
    body: Body
    headers: Headers

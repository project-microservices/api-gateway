from typing import Dict, Any, Optional
from dataclasses import dataclass

from src.app.domain.common.entities import DomainEntity
from src.app.domain.requests.value_objects import (
    Method, Path, Params, Body, Headers)


@dataclass(frozen=True)
class RequestEntity(DomainEntity[Body]):
    method: Method
    path: Path
    params: Params
    body: Body
    headers: Headers

    @staticmethod
    def create_request(
        method: str,
        path: str,
        params: Dict[str, Any],
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None
    ) -> "RequestEntity":
        return RequestEntity(
            method=Method(method),
            path=Path(path),
            params=Params(params),
            body=Body(body),
            headers=Headers(headers)
        )
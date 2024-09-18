from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class ServiceResponse:
    body: Dict[Any, Any]
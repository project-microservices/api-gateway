from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass(frozen=True)
class RequestToService:
    send_to: str
    body: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, Any]] = None
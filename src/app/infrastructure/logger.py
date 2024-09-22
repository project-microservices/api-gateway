import requests
import logging
from typing import Self, Any, Optional, Tuple, Dict, List
import time

from src.app.main.config import LokiConfig


class LokiHandler(logging.Handler):
    def __init__(
        self: Self, url: str, auth: Optional[Tuple[str, str]] = None,
        tags: Optional[Dict[str, str]] = {}
    ) -> None:
        super().__init__()
        self.url: str = url
        self.auth: Optional[Tuple[str, str]] = auth or None
        self.session: requests.Session = requests.Session()
        self.tags: Dict[str, str] = tags or {}

    def handleError(self, record: logging.LogRecord) -> None:
        return super().handleError(record)

    def emit(self, record: logging.LogRecord) -> None:
        self.tags.update(
            dict(
                severity=record.levelname.lower(),
                logger=record.name)
            )
        stream: Dict[str, Any] = dict(
            stream=self.tags,
            values=[
                [str(int(time.time() * 1e9)), self.format(record)]
            ]
        )
        try:
            self.session.auth = self.auth or None
            response: requests.Response = self.session.post(
                url=self.url, json=dict(streams=[stream])
            )
            if response.status_code != 204:
                raise Exception(response.text)
        except Exception:
            self.handleError(record=record)


def Logger(config: LokiConfig) -> logging.Logger:
    loki_handler: LokiHandler = LokiHandler(
        url=config.loki_uri,
        tags=dict(application='api-gateway-application')
    )
    logger: logging.Logger = logging.getLogger('api-gateway-logger')
    logger.addHandler(hdlr=loki_handler)
    logger.setLevel(logging.INFO)

    return logger

        


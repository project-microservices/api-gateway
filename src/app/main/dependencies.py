import logging

from src.app.infrastructure.logger import Logger
from src.app.main.config import LokiConfig


def provide_logger() -> logging.Logger:
    return Logger(
        config=LokiConfig.loki_uri_from_env()
    )

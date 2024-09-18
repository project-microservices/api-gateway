from typing import cast
from fastapi import FastAPI
from starlette.types import ExceptionHandler

from src.app.infrastructure.brokers.nats_broker import broker
from src.app.presentation.api.services.auth.routers import router
from src.app.presentation.exception_handlers import ApiError, validation_exc_handler


def get_fastapi_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    app.add_exception_handler(
        ApiError, cast(ExceptionHandler, validation_exc_handler)
    )
    return app

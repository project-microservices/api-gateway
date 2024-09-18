from typing import cast
from fastapi import FastAPI
from starlette.types import ExceptionHandler
from contextlib import asynccontextmanager
from faststream.asgi import AsgiFastStream

from src.app.infrastructure.brokers.nats_broker import broker
from src.app.presentation.api.services.auth.routers import router
from src.app.presentation.exception_handlers import validation_exc_handler
from src.app.domain.common.exceptions import DomainValidationError

@asynccontextmanager
async def lifaspan(app: FastAPI):
    get_faststream_app()
    yield

def get_faststream_app() -> AsgiFastStream:
    app = AsgiFastStream(broker, asyncapi_path='/docs')
    return app

def get_fastapi_app() -> FastAPI:
    app = FastAPI(lifespan=lifaspan)
    app.include_router(router)
    app.add_exception_handler(
        DomainValidationError, cast(ExceptionHandler, validation_exc_handler)
    )
    return app

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.app.main.dependencies import provide_logger

logger = provide_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application")
    yield

def app_factory() -> FastAPI:
    application: FastAPI = FastAPI(lifespan=lifespan)
    return application



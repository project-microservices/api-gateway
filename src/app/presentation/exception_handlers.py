from typing import cast

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler


class ApiError(Exception):
    message: str

    def __init__(self, message: str | None = None) -> None:
        super.__init__()
        if message is None:
            assert hasattr(self, "message")
        else:
            self.message = message


async def validation_exc_handler(exception: ApiError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": exception.message})

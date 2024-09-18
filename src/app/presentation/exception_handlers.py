from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.app.domain.common.exceptions import DomainValidationError


async def validation_exc_handler(
    request: Request, exception: DomainValidationError
) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": exception.message})

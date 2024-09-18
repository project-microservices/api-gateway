from typing import Annotated

from fastapi import APIRouter, Depends
from src.app.application.contracts.requests.responses import ServiceResponse
from src.app.application.contracts.requests.requests import RequestToService
from src.app.infrastructure.di.dependencies import provide_usecase
from src.app.application.usecases.request_to_service import MakeRequestToService

router = APIRouter(
    prefix="/api/auth",
    tags=["v1"],
)


@router.post('/login', response_model=ServiceResponse)
async def login(
    interactor: Annotated[MakeRequestToService, Depends(provide_usecase)]
) -> ServiceResponse:
    return await interactor(
        request=RequestToService(
            send_to='/auth/login',
            headers=None,
            body=None
        )
    )

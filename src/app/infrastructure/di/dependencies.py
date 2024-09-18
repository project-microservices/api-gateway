from src.app.application.usecases.request_to_service import MakeRequestToService
from src.app.infrastructure.brokers.publishing.publishing_service import PublishToService
from src.app.infrastructure.brokers.nats_broker import broker


def provide_usecase() -> MakeRequestToService:
    return MakeRequestToService(
        request_repository=PublishToService(
            broker=broker
        )
    )
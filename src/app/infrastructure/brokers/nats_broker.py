from faststream.nats import NatsBroker
from src.app.main.config import NatsConfig

# Нужно изменить. Глобалы-хуебалы :)

config: NatsConfig = NatsConfig.nats_uri_from_env()


def get_nats_broker(config: NatsConfig) -> NatsBroker:
    return NatsBroker(config.uri)


broker: NatsBroker = get_nats_broker(config=config)

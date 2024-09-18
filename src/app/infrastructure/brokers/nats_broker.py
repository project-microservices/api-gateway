from faststream.nats import NatsBroker
from src.app.main.config import NatsConfig

config: NatsConfig = NatsConfig.nats_uri_from_env()

def get_nats_broker(config: NatsConfig) -> NatsBroker:
    return NatsBroker("nats://localhost:4222")

broker: NatsBroker = get_nats_broker(config=config)
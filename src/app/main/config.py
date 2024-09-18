from dataclasses import dataclass
from os import environ


@dataclass(frozen=True)
class NatsConfig:
    uri: str

    @staticmethod
    def nats_uri_from_env() -> 'NatsConfig':
        uri = environ.get('NATS_URI')
        return NatsConfig(uri=str(uri))
    

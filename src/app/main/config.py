from dataclasses import dataclass
from os import environ


@dataclass(frozen=True)
class NatsConfig:
    nats_uri: str

    @staticmethod
    def nats_uri_from_env() -> 'NatsConfig':
        uri = environ.get('NATS_URI')
        return NatsConfig(uri=str(uri))


@dataclass(frozen=True)
class LokiConfig:
    loki_uri: str

    @staticmethod
    def loki_uri_from_env() -> 'LokiConfig':
        uri = environ.get('LOKI_URI')
        return LokiConfig(loki_uri=str(uri))
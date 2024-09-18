from dataclasses import dataclass
from os import environ

from dotenv import load_dotenv

load_dotenv()



@dataclass(frozen=True)
class NatsConfig:
    uri: str

    @staticmethod
    def nats_uri_from_env() -> 'NatsConfig':
        uri = environ.get('NATS_URI')
        return NatsConfig(uri=str(uri))
    

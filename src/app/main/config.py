from dataclasses import dataclass
from os import environ

from dotenv import load_dotenv


@dataclass(frozen=True)
class NatsConfig:
    load_dotenv()

    uri: str

    @staticmethod
    def nats_uri_from_env() -> 'NatsConfig':
        uri = environ.get('NATS_URI')
        return NatsConfig(uri=str(uri))


@dataclass(frozen=True)
class LoggerConfig:

    logger_conf: dict

    @staticmethod
    def get_logger_conf() -> 'LoggerConfig':
        logger_conf = {
            'version': 1,
            'formatters': {
                'console_message': {
                    'format': "{asctime} - [{levelname}] - {name} - ({filename}).{funcName}({lineno}) - {message}",
                    'style': '{',
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',  # Fixed typo
                    'level': 'INFO',
                    'formatter': 'console_message',
                }
            },
            'loggers': {
                'api-gateway-logger': {
                    'level': 'INFO',
                    'handlers': ['console']
                }
            }
        }
            
        return LoggerConfig(logger_conf=logger_conf)
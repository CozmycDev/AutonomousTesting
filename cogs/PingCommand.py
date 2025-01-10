from logging.handlers import RotatingFileHandler
import logging

file_config = {
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': '/var/log/ping.log',
    'mode': 'a',
    'level': 'INFO',
    'formatter': 'verbose',
    'maxBytes': 1024 * 1024,  # 1MB
    'backupCount': 5
}

class LoggingConfig:
    def __init__(self, handlers=None, formatters=None):
        self.handlers = handlers if handlers else handler_config
        self.formatters = formatters if formatters else formatters

logging.config.dictConfig(self.LoggingConfig())
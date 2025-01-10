import logging
from typing import Dict

class FileHandler(logging.Handler):
    def __init__(self, filename: str, mode: str = 'a'):
        super().__init__()
        self.filename = filename
        self.mode = mode

    def emit(self, record) -> None:
        message = self.format(record)
        with open(self.filename, self.mode) as log_file:
            log_file.write(message + '\n')

def configure_logging(filename: str, log_level: str, mode: str = 'a') -> logging.Handler:
    handler = FileHandler(filename, mode)

    # Configure the logging module with the chosen log level
    logging.basicConfig(level=get_log_level(log_level))

    return handler

def get_log_level(log_level: str) -> int:
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    if log_level in level_map:
        return level_map[log_level]
    else:
        raise ValueError(f"Invalid log level: {log_level}")

# Set the default logging level
log_level = set_default_log_level()

# Configure the logging module with the chosen log level
handler = configure_logging('log.txt', log_level)

# Create a logger instance
logger = logging.getLogger(__name__)

# Add the handler to the logger
logger.addHandler(handler)
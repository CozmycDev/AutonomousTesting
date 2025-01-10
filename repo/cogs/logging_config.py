import logging
from typing import Dict

class FileHandler(logging.Handler):
    def __init__(self, filename: str, mode: str = 'a'):
        super().__init__()
        self.filename = filename
        self.mode = mode

    def emit(self, record) -> None:
        message = self.format(record)
        with open(self.filename, self.mode + 'b') as log_file:  
            log_file.write(message.encode('utf-8') + b'\n')

def configure_logging(filename: str, log_level: str, mode: str = 'a') -> logging.Handler:
    handler = FileHandler(filename, mode)

    logger = logging.getLogger()
    logger.setLevel(get_log_level(log_level))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(handler)

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

def set_default_log_level() -> int:
    log_level = 'INFO'
    return get_log_level(log_level)

# Create a logger instance
logger = configure_logging('log.txt', 'INFO')
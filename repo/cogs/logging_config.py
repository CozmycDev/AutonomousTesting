from pathlib import Path
import logging

class FileHandler(logging.Handler):
    def __init__(self, filename: str, mode: str = 'a'):
        super().__init__()
        self._filename = Path(filename)
        self.mode = _check_mode(mode)

    @staticmethod
    def _check_mode(mode: str) -> str:
        if not isinstance(mode, str):
            raise ValueError("Mode must be a string.")
        
        if len(mode) < 1 or mode[-1] != 'b':
            return 'a'
        else:
            # Add the file extension to prevent opening binary files
            return mode[:-1] + '.txt'

    def emit(self, record) -> None:
        message = self.format(record)
        with open(str(self._filename), self.mode, encoding='utf-8') as log_file:  
            log_file.write(message + '\n')

def configure_logging(filename: str, log_level: str, mode: str = 'a') -> logging.Handler:
    handler = FileHandler(filename, mode)

    logger = logging.getLogger()
    if not logger.hasHandlers():
        logger.setLevel(get_log_level(log_level))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
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
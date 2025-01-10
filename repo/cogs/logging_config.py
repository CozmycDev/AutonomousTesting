def log_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write('\n')
    except FileNotFoundError:
        print(f"Failed to create {filename}")

def set_default_log_level():
    return "INFO"

# Set the default logging level
log_level = set_default_log_level()

# Configure the logging module with the chosen log level
import logging
logging.basicConfig(level=log_level)

# Create a custom logging handler for file logging
class FileHandler(logging.Handler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a') as log_file:
            log_file.write(message + '\n')

# Create a file handler and add it to the logging module
log_handler = FileHandler('log.txt')
logging.addHandler(log_handler)
file_config = {
    'class': 'logging.handlers.TimedRotatingFileHandler',
    'filename': '/var/log/ping.log',
    'mode': 'a',
    'level': 'INFO',
    'when': 'midnight',
    'interval': 1,
    'backupCount': 5
}
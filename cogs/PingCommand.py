logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/ping.log',
            'mode': 'a',
            'level': 'INFO',
            'formatter': 'verbose'
        }
    }

handler_config = [
    {'name': 'console', 'level': 'DEBUG'},
    {'name': 'file', 'level': 'INFO'}
]

formatters = {
    'simple': {
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    },
    'verbose': {
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(funcName)s - %(message)s'
    }
}

class LoggingConfig:
    def __init__(self, handlers=None, formatters=None):
        self.handlers = handlers if handlers else handler_config
        self.formatters = formatters if formatters else formatters

logging.config.dictConfig(selfLoggingConfig())
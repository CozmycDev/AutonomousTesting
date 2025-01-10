logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        }
    },
    'loggers': {
        __name__: {
            'level': 'INFO',
            'propagate': True,
            'handlers': ['console']
        }
    }
}

# END_FILE
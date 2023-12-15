from .base import *  # noqa

import os

DEBUG = False

STATIC_ROOT = '/media/demo-portifolio-dev/staticfiles/'
MEDIA_ROOT = '/media/demo-portifolio-dev/media/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/root/logs/demos/portifolio-dev/debug.log',
        },
        'file_info': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename':  '/root/logs/demos/portifolio-dev/debug_info.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'members_enable': {
            'handlers': ['file_info'],
            'level': 'INFO',
        },
    },
}

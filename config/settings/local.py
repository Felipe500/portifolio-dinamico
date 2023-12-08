from .base import *  # noqa

import os

DEBUG = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'statics'))]

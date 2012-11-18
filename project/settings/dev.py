from os import path

from settings import APP_DIR
from settings.base import INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(APP_DIR, 'data', 'dev.db'),
    }
}

DEBUG = TEMPLATE_DEBUG = True
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda: True,
}

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'debug_toolbar',
]

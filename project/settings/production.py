import os

from memcacheify import memcacheify
from postgresify import postgresify

from settings.base import INSTALLED_APPS

DATABASES = postgresify()
CACHES = memcacheify()

SECRET_KEY = os.environ.get('SECRET_KEY')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda: False,
}

SITE_ID = 3

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'gunicorn',
]

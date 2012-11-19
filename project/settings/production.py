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

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'gunicorn',
]

DOMAIN = 'https://itu-production.herokuapp.com'

# Staticfiles settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
AWS_ACCESS_KEY_ID = 'AKIAJ26VA4NJKAH4DQSQ'
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = 'fftf.itu'
AWS_S3_CUSTOM_DOMAIN = "s3.amazonaws.com/fftf.itu"
STATIC_URL = 'https://s3.amazonaws.com/fftf.itu/'

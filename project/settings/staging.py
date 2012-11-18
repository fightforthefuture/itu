from settings.production import *

SITE_ID = 2

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'debug_toolbar',
]

AWS_STORAGE_BUCKET_NAME = 'fftf.itu.staging'
AWS_S3_CUSTOM_DOMAIN = "s3.amazonaws.com/fftf.itu.staging"
STATIC_URL = 'https://s3.amazonaws.com/fftf.itu.staging/'

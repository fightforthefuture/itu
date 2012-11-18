from settings.production import *

SITE_ID = 2

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'debug_toolbar',
]

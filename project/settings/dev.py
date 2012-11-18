from os import path
from settings import APP_DIR

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

import os

from settings import APP_DIR


# Path settings
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(APP_DIR, 'static'),
)
ADMIN_MEDIA_PREFIX = '%sadmin/' % STATIC_URL
MEDIA_ROOT = os.path.join(APP_DIR, 'media')
MEDIA_URL = '/media/'
TEMPLATE_DIRS = (
    os.path.join(APP_DIR, 'templates'),
)
FIXTURE_DIRS = ()


# Debugging settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Chuck Harmston', 'chuck@chuckharmston.com'),
)
MANAGERS = ADMINS


# Localization settings
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = False
LANGUAGE_CODE = 'en-us'


# Apps, classes, processors, and loaders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'debug_toolbar',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# Misc. settings
SITE_ID = 1
SECRET_KEY = 'dskba^j4%zysn*d-+yh!w!2_vd938d2pia0dk0v40yie^t!tc$'
ROOT_URLCONF = 'project.urls'
INTERNAL_IPS = ('127.0.0.1',)

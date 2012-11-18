import os

from settings import APP_DIR


gettext = lambda s: s


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
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', gettext('English')),
    ('is', gettext('Icelandic')),
)
LOCALE_PATHS = (
    os.path.join(APP_DIR, 'apps', 'itu', 'locale',),
)
GEOIP_DATA = os.path.join(APP_DIR, 'data', 'GeoLiteCity.dat')
GEOIP_SESSION_FIELDS = [
    'country_name',
    'region_name',
    'city',
]

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
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'ip2geo.middleware.CityMiddleware',
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
    'itu',
    'ip2geo',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'context_processors.domain',
    'ip2geo.context_processors.add_session',
)


# Misc. settings
SITE_ID = 1
SECRET_KEY = 'dskba^j4%zysn*d-+yh!w!2_vd938d2pia0dk0v40yie^t!tc$'
ROOT_URLCONF = 'project.urls'
INTERNAL_IPS = ('127.0.0.1',)

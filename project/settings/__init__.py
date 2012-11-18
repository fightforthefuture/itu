import os
from sys import path as pythonpath

# Base application directory
APP_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
))

# Update $PYTHONPATH to include apps, project, and settings directories
pythonpath.insert(1, os.path.join(APP_DIR, 'apps'))
pythonpath.insert(2, os.path.join(APP_DIR, 'project'))
pythonpath.insert(3, os.path.join(APP_DIR, 'project', 'settings'))

# Import base settings
base = __import__('project.settings.base', {}, {}, ['base'], -1)
for setting in dir(base):
    if setting == setting.upper():
        locals().update({setting: getattr(base, setting)})


# Allow environment to be defined by either environment variable (set in, e.g.,
# a WSGI script) or via hostname.
env_name = os.environ.get('ENVIRONMENT', 'dev')


# Import environment settings
try:
    print 'Loading %s settings' % env_name
    environment_settings = __import__(
        'project.settings.%s' % env_name,
        globals(),
        locals(),
        [env_name],
        -1
    )
except ImportError:
    raise ImportError('Error loading %s settings' % env_name)
else:
    for setting in dir(environment_settings):
        if setting == setting.upper():
            locals().update({
                setting: getattr(environment_settings, setting)
            })

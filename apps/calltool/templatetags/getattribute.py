import re
from django import template
from django.conf import settings

register = template.Library()


def getattribute(value, arg):
    """
    Gets an attribute of an object dynamically from a string name.
    """
    numeric_test = re.compile("^\d+$")
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and arg in value:
        return value[arg]
    elif numeric_test.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID

register.filter('getattribute', getattribute)

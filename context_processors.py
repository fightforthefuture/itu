from django.conf import settings


def domain(request):
    return {
        'DOMAIN': getattr(settings, 'DOMAIN', None)
    }

from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic.base import TemplateView

from calltool.views import CallInfoView, CallToolView
from itu.views import MainView, SetLanguageView, WidgetView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^language/$', SetLanguageView.as_view(), name='set_language'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^calltool/twiml/(?P<country>[^\/]+)/$', CallInfoView.as_view(), name='twiml'),
    url(r'^calltool/$', CallToolView.as_view(), name='calltool'),
    url(r'^thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    url(r'^widget/', WidgetView.as_view(), name='widget'),
    url(r'^$', MainView.as_view(), name='main'),
)

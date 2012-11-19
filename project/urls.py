from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from calltool.views import CallInfoView, CallToolView
from itu.views import LyricsView, SetLanguageView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^language/$', SetLanguageView.as_view(), name='set_language'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^calltool/twiml/(?P<country>[^\/]+)/$', CallInfoView.as_view(), name='twiml'),
    url(r'^calltool/$', CallToolView.as_view(), name='calltool'),
    url(r'^$', LyricsView.as_view(), name='lyrics'),
)

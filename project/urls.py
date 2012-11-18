from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns

from itu.views import LyricsView, SetLanguageView


urlpatterns = patterns('',
    url(r'^language/$', SetLanguageView.as_view(), name='set_language'),
)

urlpatterns += i18n_patterns('',
    url(r'^$', LyricsView.as_view(), name='lyrics'),
)

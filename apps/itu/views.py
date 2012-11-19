from django.conf import settings
from django.utils.translation import check_for_language
from django.views.generic.base import RedirectView, TemplateView


class LyricsView(TemplateView):
    template_name = 'lyrics.html'


class SetLanguageView(RedirectView):
    permanent = True
    query_string = True

    def post(self, request, *args, **kwargs):
        response = super(SetLanguageView, self).post(request, *args, **kwargs)
        lang_code = request.POST.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response

    def get_redirect_url(self):
        next = self.request.REQUEST.get('next', None)
        if not next:
            next = self.request.META.get('HTTP_REFERER', None)
        if not next:
            next = '/'
        return next
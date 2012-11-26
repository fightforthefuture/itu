from django.conf import settings
from django.utils.translation import check_for_language
from django.views.generic.base import RedirectView, TemplateView

from django_countries.countries import COUNTRIES as ALL_COUNTRIES

from calltool.choices import AUTORESPONDER_IDS


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


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['all_countries'] = ALL_COUNTRIES
        context['autoresponder_ids'] = AUTORESPONDER_IDS
        import pdb
        pdb.set_trace()
        return context

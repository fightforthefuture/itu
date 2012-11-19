from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.safestring import mark_safe

from twilio import twiml

from calltool.client import client
from calltool.forms import CallToolForm
from calltool.models import PhoneNumber


class CallInfoView(TemplateView):
    template_name = 'twiml.xml'

    def get_context_data(self, **kwargs):
        context = super(CallInfoView, self).get_context_data(**kwargs)
        context['twiml'] = self._twiml()
        return context

    def _number(self):
        country = self.kwargs['country'].upper()
        return PhoneNumber.objects.filter(country=country).order_by('?')[0]

    def _twiml(self):
        phone_number = self._number()
        response = twiml.Response()
        response.say((
            'Connecting you to your ITU representative, %s. Please hold.'
        ) % phone_number.name)
        response.dial(number=phone_number.number)
        return mark_safe(str(response))

    def render_to_response(self, context, **kwargs):
        return super(CallInfoView, self).render_to_response(context,
            content_type='application/xml',
            **kwargs
        )


class CallToolView(FormView):
    template_name = 'calltool.html'
    form_class = CallToolForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form_data = self.get_form_kwargs()['data']
        call = client.calls.create(
            to=form_data['number'],
            from_='6122463812',
            url=settings.DOMAIN + reverse('twiml', kwargs={
                'country': form_data['country']
            }),
        )
        return super(CallToolView, self).form_valid(form)

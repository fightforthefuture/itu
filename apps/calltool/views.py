from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
        return PhoneNumber.objects.filter(country=country).order_by('?')

    def _twiml(self):
        phone_number = self._number()
        if(len(phone_number)):
            return self._has_contact(phone_number[0])
        else:
            return self._no_contact()

    def _has_contact(self, phone_number):
        response = twiml.Response()
        response.say((
            'Connecting you to your ITU representative, %s. Please hold.'
        ) % phone_number.name)
        response.dial(number=phone_number.number)
        return mark_safe(str(response))

    def _no_contact(self):
        response = twiml.Response()
        response.say((
            'Unfortunately, your country has no ITU representative.'
        ))
        return mark_safe(str(response))

    def render_to_response(self, context, **kwargs):
        return super(CallInfoView, self).render_to_response(context,
            content_type='application/xml',
            **kwargs
        )


class CallToolView(FormView):
    template_name = 'calltool.html'
    form_class = CallToolForm

    def get_success_url(self):
        form_data = self.get_form_kwargs()['data']
        return reverse('twiml', kwargs={
            'country': form_data['country']
        })

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CallToolView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form_data = self.get_form_kwargs()['data']
        client.calls.create(
            to=form_data['number'],
            from_='4133972653',
            url='https://itu-production.herokuapp.com' + reverse('twiml', kwargs={
                'country': form_data['country']
            }),
            method='GET',
        )
        return super(CallToolView, self).form_valid(form)

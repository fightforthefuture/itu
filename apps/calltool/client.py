from twilio.rest import TwilioRestClient

from django.conf import settings


client = TwilioRestClient(settings.TWILIO_ACCOUNT, settings.TWILIO_AUTH_TOKEN)

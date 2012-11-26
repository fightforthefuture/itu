from django import forms

from django_countries.countries import COUNTRIES as ALL_COUNTRIES


class CallToolForm(forms.Form):
    country = forms.ChoiceField(choices=ALL_COUNTRIES)
    number = forms.IntegerField()
    extension = forms.CharField(max_length=34, required=False)

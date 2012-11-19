from django import forms

from calltool.countries import COUNTRIES


class CallToolForm(forms.Form):
    country = forms.ChoiceField(choices=COUNTRIES)
    number = forms.IntegerField()
    extension = forms.CharField(max_length=34, required=False)

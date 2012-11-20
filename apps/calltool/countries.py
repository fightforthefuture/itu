from calltool.models import PhoneNumber

from django_countries.countries import COUNTRIES as ALL_COUNTRIES


# List of unique countries that have phone numbers, sorted by name
used_countries = set([pn.country for pn in PhoneNumber.objects.all()])
all_countries = dict(ALL_COUNTRIES)
COUNTRIES = []

for country in used_countries:
    COUNTRIES.append((country, all_countries[country],))

COUNTRIES.sort()

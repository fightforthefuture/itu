from django.db import models

from django_countries.countries import COUNTRIES


class PhoneNumber(models.Model):
    country = models.CharField(max_length=8, choices=COUNTRIES)
    number = models.CharField(max_length=32)
    name = models.CharField('Name and title', max_length=128)
    extension = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        if self.extension:
            return '%s: %s x%s' % (self.country, self.number, self.extension)
        else:
            return '%s: %s' % (self.country, self.number,)

import re

from django.db import models

from django_countries.countries import COUNTRIES


class PhoneNumber(models.Model):
    country = models.CharField(max_length=8, choices=COUNTRIES)
    number = models.CharField('Phone Number',
        max_length=32,
        help_text='All non-numeric characters are automatically removed.'
    )
    name = models.CharField('Name and title',
        max_length=128,
        help_text=(
            'Will be read by a computerized voice, so please write this as '
            'you would speak it (without abbreviations, etc).'
        )
    )

    def __unicode__(self):
        return '%s (%s): %s' % (self.name, self.country, self.number,)

    class Meta:
        ordering = ['country']

    def clean(self):
        """
        Strip sall non-numeric characters from the phone number.
        """
        self.number = re.sub(r'\D', '', self.number)

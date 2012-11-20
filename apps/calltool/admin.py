from django.contrib import admin

from calltool.models import PhoneNumber


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    list_filter = ('country',)
    search_fields = ('name', 'country', 'number',)

admin.site.register(PhoneNumber, PhoneNumberAdmin)

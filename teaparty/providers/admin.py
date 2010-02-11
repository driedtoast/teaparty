from teaparty.providers.models import ProviderType
from django.contrib import admin


class ProviderTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['type']}),
        ('API information', {'fields': ['providerClass']}),
    ]
    list_display = ('type', 'providerClass')

admin.site.register(ProviderType,ProviderTypeAdmin)

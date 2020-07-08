from django.contrib import admin

# Register your models here.
from .models import Site, Framework, Provider

class SiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'name')
    list_filter = ['name']
    search_fields = ['name']


class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('site', 'app', 'ver', 'type', 'date')
    list_filter = ['site', 'type']


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('site', 'provider', 'ip', 'source')
    list_filter = ['provider', 'source']


admin.site.register(Site, SiteAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Provider, ProviderAdmin)

from django.contrib import admin

# Register your models here.
from .models import Site, Framework

class SiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'name')
    list_filter = ['name']
    search_fields = ['name']


class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('site','app','ver','type','date')
    list_filter = ['site','type']


admin.site.register(Site, SiteAdmin)
admin.site.register(Framework, FrameworkAdmin)

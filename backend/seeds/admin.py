from django.contrib import admin

from .models import Seed, Type


class SeedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'type',) 
    search_fields = ('type',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


admin.site.register(Seed, SeedAdmin)
admin.site.register(Type, TypeAdmin)

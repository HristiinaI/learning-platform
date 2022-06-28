from django.contrib import admin

from .models import Carusel

class CaruselAdmin(admin.ModelAdmin):
    fields = ['title', 'dеscription', 'link', 'image']
    list_display = ['title']
    search_fields = ['title']

admin.site.register(Carusel, CaruselAdmin)

from django.contrib import admin
from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = [
        'make',
        'model',
    ]

admin.site.register(Car,CarsAdmin)


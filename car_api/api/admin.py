from django.contrib import admin
from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'make',
        'model',
    ]
class RatingsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'car',
        'rating',
    ]

admin.site.register(Car,CarsAdmin)
admin.site.register(Rating,RatingsAdmin)


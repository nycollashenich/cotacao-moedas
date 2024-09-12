from django.contrib import admin
from .models import Conversion

@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ['from_currency', 'to_currency', 'conversion_date']

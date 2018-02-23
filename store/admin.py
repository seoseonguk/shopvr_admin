from django.contrib import admin
from .models import Store, TimeSales



class TimeSalesAdmin(admin.ModelAdmin):
    list_display = ['__str__','sales']

# Register your models here.
admin.site.register(Store)
admin.site.register(TimeSales,TimeSalesAdmin)
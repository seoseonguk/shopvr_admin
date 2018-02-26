from django.contrib import admin
from .models import Store, TimeSales, DailySales



class TimeSalesAdmin(admin.ModelAdmin):
    list_display = ['__str__','sales']

class DailySalesAdmin(admin.ModelAdmin):
    list_display = ['__str__','total_sales']


# Register your models here.
admin.site.register(Store)
admin.site.register(TimeSales,TimeSalesAdmin)
admin.site.register(DailySales,DailySalesAdmin)

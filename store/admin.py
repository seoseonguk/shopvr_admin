from django.contrib import admin
from .models import Store, TimeSales, TestForKorean



class TimeSalesAdmin(admin.ModelAdmin):
    list_display = ['__str__','sales']

# Register your models here.
admin.site.register(Store)
admin.site.register(TimeSales,TimeSalesAdmin)

admin.site.register(TestForKorean)
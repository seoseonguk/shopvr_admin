from django.contrib import admin
from .models import MarketingArea, MarketingAreaTag, Location, SubwayStation, University
# Register your models here.

class SubwayStationAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(SubwayStation, SubwayStationAdmin)
admin.site.register(MarketingArea)
admin.site.register(MarketingAreaTag)
admin.site.register(Location)
admin.site.register(University)
from django.contrib import admin
from .models import SubwayStation, MarketingArea, MarketingAreaTag, Location
# Register your models here.
admin.site.register(SubwayStation)
admin.site.register(MarketingArea)
admin.site.register(MarketingAreaTag)
admin.site.register(Location)
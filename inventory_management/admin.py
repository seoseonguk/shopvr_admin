from django.contrib import admin
from .models import Order, Item, Item_Category
# Register your models here.

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Item_Category)
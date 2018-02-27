from django.contrib import admin
from .models import Order, Product, Product_Category, OrderedProduct
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Product_Category)
admin.site.register(OrderedProduct)
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .validators import *

# Create your models here.................
class Order(models.Model):
    store = models.CharField(max_length=100, validators=[min_length_2_validator])
    user = models.ForeignKey(User, on_delete=models.SET(1))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.store

    def get_absolute_url(self):
        return reverse('inventory:order_detail', args=[self.id])

class Item_Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    item_category = models.ForeignKey('Item_Category',null=True, on_delete=models.SET_NULL)
    supply_price = models.IntegerField()
    delivery_price = models.IntegerField()
    available_stock = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    recommended_stock = models.IntegerField()
    supplier = models.CharField(blank=True, max_length=20)
    user_agent = models.CharField(max_length=200)

    def __str__(self):
        return self.name
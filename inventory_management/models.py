from django.db import models
from django.urls import reverse
from .validators import *

# Create your models here.................
class Order(models.Model):
    store = models.CharField(max_length=100, validators=[min_length_2_validator])
    extra = models.TextField()
    coffee_bean = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.store

    def get_absolute_url(self):
        return reverse('inventory:order_detail', args=[self.id])


class Item(models.Model):
    name = models.CharField(max_length=20)
    supply_price = models.IntegerField()
    delivery_price = models.IntegerField()
    available_stock = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
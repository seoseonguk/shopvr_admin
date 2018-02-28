from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .validators import *


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PriceModel(models.Model):
    class Meta:
        abstract = True

    supply_price = models.IntegerField()
    delivery_price = models.IntegerField()


class OrderStatusModel(models.Model):
    class Meta:
        abstract = True

    STATUS_CHOICES = [
        ('processing', '주문 진행 중'),
        ('cancelled', '주문 취소됨'),
        ('order-complete', '발주 완료'),
        ('deliverying', '배송중'),
        ('delivered', '배송완료'),
        ('complete', '정상수령'),
        ('returned', '반품수거'),
        ('missing', '주문누락')
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

# Create your models here.................
class Order(TimeStampedModel, OrderStatusModel):
    store = models.CharField(max_length=100, validators=[min_length_2_validator])
    user = models.ForeignKey(User, on_delete=models.SET(1))

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.store

    def get_absolute_url(self):
        return reverse('inventory:order_detail', args=[self.id])


class Product_Category(TimeStampedModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(TimeStampedModel, PriceModel):
    name = models.CharField(max_length=20)
    item_category = models.ForeignKey('Product_Category',null=True, on_delete=models.SET_NULL)
    available_stock = models.IntegerField()
    recommended_stock = models.IntegerField()
    supplier = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:item_detail', args=[self.id])

class OrderedProduct(TimeStampedModel, PriceModel):
    class Meta:
        verbose_name = "주문한 제품"
        verbose_name_plural = verbose_name

    order = models.ForeignKey(Order, verbose_name='주문서', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='제품', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
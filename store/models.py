from django.db import models
from core.models import TimeStampedModel




class BaseStoreModel(models.Model):
    class Meta:
        abstract = True
    STORE_CHOICES =    [
        ('hd1', '홍대 1호점'),
        ('hd2', '홍대 2호점'),
        ('sc', '신촌점'),
        ('bp', '부평점'),
        ('sw', '수원역점'),
        ('sh', '서현점')
    ]
    store = models.CharField('매장', max_length=10, choices=STORE_CHOICES)

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    slug = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    # phone number validator
    open_date = models.DateField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class DailySales(models.Model):
    class Meta:
        unique_together = ('store','date')

    pos_cash_sales = models.IntegerField(null=True)
    pos_card_sales = models.IntegerField(null=True)
    kiosk_cash_sales = models.IntegerField(null=True)
    kiosk_card_sales =models.IntegerField(null=True)
    total_sales = models.IntegerField(null=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    date = models.DateField()
    weekday = models.CharField(max_length=10)

    def __str__(self):
        return ("{} - {}".format(self.store, self.date))


class TimeSales(models.Model):
    class Meta:
        unique_together = ('store', 'time')

    time = models.DateTimeField()
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    sales = models.IntegerField(null=True)
    count = models.SmallIntegerField(null=True)

    def __str__(self):
        return ("{} - {}".format(self.store, self.time))


class NaverSearching(BaseStoreModel, TimeStampedModel):
    date = models.DateField()
    keyword = models.CharField(max_length=20)
    occupied = models.CharField(max_length=300)
    percent_first_page = models.FloatField(max_length=10)
    percent_for_all = models.FloatField(max_length=10)
    is_mobile = models.BooleanField(default=0)

    def __str__(self):
        return ("{}({}) - {}".format(self.store , self.keyword, self.date))

    class Meta:
        verbose_name = "네이버 블로그 검색 결과"
        verbose_name_plural = verbose_name
        unique_together = ('store', 'date', 'keyword', 'is_mobile')


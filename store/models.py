from django.db import models

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
    time = models.DateTimeField()
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    sales = models.IntegerField(null=True)
    count = models.SmallIntegerField(null=True)

    def __str__(self):
        return ("{} - {}".format(self.store, self.time))

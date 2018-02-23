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

class TimeSales(models.Model):
    time = models.DateTimeField()
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    sales = models.IntegerField(blank=True)
    count = models.SmallIntegerField(blank=True)

    def __str__(self):
        return ("{} - {}".format(self.store, self.time))
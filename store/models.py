from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # phone number validator
    open_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
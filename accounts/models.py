from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete='CASCADE')
    phone_number = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    store = models.CharField(max_length=20)

    def __str__(self):
        return self.user.__str__()

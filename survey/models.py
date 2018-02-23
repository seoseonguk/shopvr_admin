from django.db import models
from django.conf import settings
from store.models import Store
# Create your models here.

AGE_TYPE_CHOICES = (
    (10, '-12'),
    (15, '12-19'),
    (21, '20-23'),
    (25, '23-28U(대학생)'),
    (26, '23-28E(직장인)'),
    (32, '28+'),
    (38, '35+')
)

CUSTOMER_TYPE_CHOICES = (
    ('MF', 'MALE+FEMALE'),
    ('FF', 'FEMALE+FEMALE'),
    ('MM', 'MALE+MALE'),
    ('M+', 'MALE+'),
    ('F+', 'FEMALE+'),
    ('FAM', 'FAMILY'),
    ('G3+', 'GROUP3+'),
    ('G5+', 'GROUP5+')
)

class Question(models.Model):
    title = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return  self.title


class Survey(models.Model):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField(choices=AGE_TYPE_CHOICES, default=25)
    type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES, default='MF')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("{} 지점 @{}".format(self.store,self.created_date))

class Answer(models.Model):
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return (self.question + self.answer)
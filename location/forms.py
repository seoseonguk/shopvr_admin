from django import forms
from .models import Location, MarketingArea
from .naver_map_point_widget import NaverMapPointWidget

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'lnglat': NaverMapPointWidget()
        }



class MarketingAreaForm(forms.ModelForm):
    class Meta:
        model = MarketingArea
        fields = '__all__'
        widgets = {
            'lnglat': NaverMapPointWidget()
        }


# class Location(TimeStampedModel, AddressModel):
#     nickname = models.CharField(max_length=20)
#
#
#     deposit = models.IntegerField()
#     premium_deposit = models.IntegerField()
#     monthly_rent_fee = models.IntegerField()
#     maintainence_cost = models.IntegerField()
#
#     contact_info = models.CharField(max_length=100)
#
#
#     def __str__(self):
#         return self.nickname
#

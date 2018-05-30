from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AddressModel(models.Model):
    class Meta:
        abstract = True

    address = models.TextField(blank=True)
    # x_axis = models.CharField(max_length=20)
    # y_axis = models.CharField(max_length=20)
    lnglat = models.CharField(max_length=50)

    provinence = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=10)
    district_county_town = models.CharField(max_length=10, blank=True)
    neighborhood_township_village = models.CharField(max_length=10)
    additional_address =  models.CharField(max_length=100, blank=True)
    level = models.IntegerField(blank=True)


class SubwayStation(TimeStampedModel):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=10)

    def __str__(self):
        return "{} 호선 {} 역".format(self.category, self.title)

LOCATION_CLASS_CHOICES = {
    ('LV','주거'),
    ('UV','대학'),
    ('TF','교통'),
    ('OF','오피스')
}

COMSUMPTION_PROPENSITY_CHOICES = {
    ('OVERALL','종합'),
    ('ENTERTAINMENT','유흥'),
    ('DATING','데이트'),
    ('SHOPPING','쇼핑')

}

LOCATION_GRADE_CHOICES = {
    ('S','S'),
    ('A','A'),
    ('B','B'),
    ('C','C')
}

class MarketingArea(TimeStampedModel, AddressModel):
    title= models.CharField(max_length=20)
    location_class = models.CharField(max_length=20, choices=LOCATION_CLASS_CHOICES)
    comsumption_propensity = models.CharField(max_length=20, choices=COMSUMPTION_PROPENSITY_CHOICES)
    subway_station =  models.ManyToManyField('SubwayStation')
    location_point = models.IntegerField()
    location_grade = models.CharField(max_length=20, choices=LOCATION_GRADE_CHOICES)




    escape_room = models.IntegerField()
    animal_cafe = models.IntegerField()
    healing_cafe = models.IntegerField()
    comic_book_cafe = models.IntegerField()
    arrow_cafe = models.IntegerField()

    def __str__(self):
        return self.title


class MarketingAreaTag(TimeStampedModel):
    title = models.CharField(max_length=20)


class Location(TimeStampedModel, AddressModel):
    nickname = models.CharField(max_length=20)


    deposit = models.IntegerField()
    premium_deposit = models.IntegerField()
    monthly_rent_fee = models.IntegerField()
    maintainence_cost = models.IntegerField()

    contact_info = models.CharField(max_length=100)


    def __str__(self):
        return self.nickname


class Competitor(TimeStampedModel, AddressModel):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    marketing_area = models.ForeignKey('MarketingArea', on_delete=models.CASCADE)
    open_date = models.DateField(blank=True)
    fee_for_couple = models.PositiveIntegerField()
    operating_time_weekday = models.CharField(max_length=100)
    operating_time_weekend = models.CharField(max_length=100)
    is_steam_based = models.BooleanField()
    is_drink_essential = models.BooleanField()
    is_atraction_operating = models.CharField(max_length=100)
    grade = models.IntegerField()
    blog_link = models.URLField(max_length=100)
    etc = models.TextField()


    def __str__(self):
        return self.title



class SalesModel(models.Model):
    class Meta:
        abstract = True

    sales = models.IntegerField()

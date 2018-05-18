from django.db import models



class Location(models.Model):
    nickname = models.CharField(max_length=20)
    provinence = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=10)
    district_county_town = models.CharField(max_length=10, blank=True)
    neighborhood_township_village = models.CharField(max_length=10)

    address = models.TextField(blank=True)
    x_axis = models.CharField(max_length=20)
    y_axis = models.CharField(max_length=20)

    location_class = models.CharField(max_length=20)
    location_grade = models.CharField(max_length=20)




    escape_room = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nickname


class LocationTag(models.Model):
    title = models.CharField(max_length=20)
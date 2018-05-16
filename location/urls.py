from django.urls import path
from . import views

app_name = 'location'
urlpatterns = [
    path('new', views.LocationCreateView.as_view(), name='location_new')
]
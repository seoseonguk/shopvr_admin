from django.urls import path
from . import views

app_name = 'location'
urlpatterns = [
    path('',views.LocationListView.as_view(),name='location_list'),
    path('new', views.LocationCreateView.as_view(), name='location_new')
]
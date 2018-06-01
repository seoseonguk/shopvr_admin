from django.urls import path
from .views import (LocationListView,
                    LocationCreateView,
                    MarketingAreaCreateView,
                    MarketingAreaListView,
                    UniversityDetailView,
                    UniversityListView,
                    SubwayStationListView,
                    SubwayStationDetailView)

app_name = 'location'
urlpatterns = [
    path('',LocationListView.as_view(),name='location_list'),
    path('new', LocationCreateView.as_view(), name='location_new'),

    path('ma/', MarketingAreaListView.as_view(), name='marketingarea_list'),
    path('ma/new', MarketingAreaCreateView.as_view(), name='marketingarea_new'),

    path('univ/',UniversityListView.as_view(), name='univ_list'),
    path('univ/<int:pk>', UniversityDetailView.as_view(), name='univ_detail'),

    path('subway/', SubwayStationListView.as_view(), name='subway_list'),
    path('subway/<int:pk>', SubwayStationDetailView.as_view(), name='subway_detail'),

]

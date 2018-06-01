from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Location, MarketingArea, University, SubwayStation
from .forms import LocationForm, MarketingAreaForm
# Create your views here.


class LocationListView(ListView):
    model = Location


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('location:location_list')


class MarketingAreaListView(ListView):
    model = MarketingArea


class MarketingAreaCreateView(CreateView):
    model = MarketingArea
    form_class = MarketingAreaForm


class UniversityListView(ListView):
    model = University


class UniversityDetailView(DetailView):
    model = University



class SubwayStationListView(ListView):
    model = SubwayStation


class SubwayStationDetailView(DetailView):
    model = SubwayStation
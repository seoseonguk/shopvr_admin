from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Location, MarketingArea
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
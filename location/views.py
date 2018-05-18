from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Location
from .forms import LocationForm
# Create your views here.


class LocationListView(ListView):
    model = Location


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('inventory:item_list')

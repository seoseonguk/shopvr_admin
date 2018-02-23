from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import TimeSales, Store
# Create your views here.


class TimeSalesListView(ListView):
    model = TimeSales

    def get_queryset(self):
        self.store = get_object_or_404(Store, slug=self.kwargs['store'])
        print(self.store)
        return TimeSales.objects.filter(store=self.store)



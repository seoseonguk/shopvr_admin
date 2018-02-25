from django.urls import path
from .views import TimeSalesListView, update_time_sales

app_name = 'store'
urlpatterns =[
    path('sales/update', update_time_sales),
    path('sales/', TimeSalesListView.as_view(), name='time_sales_list'),
]
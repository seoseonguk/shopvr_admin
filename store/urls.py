from django.urls import path
from .views import TimeSalesListView, update_time_sales, DailySalesListView, update_daily_sales

app_name = 'store'
urlpatterns =[
    path('sales/time/update', update_time_sales),
    path('sales/day', DailySalesListView.as_view(), name='daily_sales_list'),
    path('sales/day/update', update_daily_sales),
    path('sales/time', TimeSalesListView.as_view(), name='time_sales_list'),

]
from django.urls import path
from .views import TimeSalesListView, update_time_sales, DailySalesListView, update_daily_sales, DailySalesAnalysisView, SCDailySalesListView, BPDailySalesListView,DailySalesForAllStoreListView

app_name = 'store'
urlpatterns =[
    path('sales/time/update', update_time_sales),
    path('sales/day', DailySalesListView.as_view(), name='daily_sales_list'),
    path('sales/day/all',DailySalesForAllStoreListView.as_view(), name='daily_sales_all_list'),
    path('sales/day/update', update_daily_sales),
    path('sales/time', TimeSalesListView.as_view(), name='time_sales_list'),
    path('sales/analysis', DailySalesAnalysisView.as_view(), name='sales_analysis'),




    path('sc/sales/day', SCDailySalesListView.as_view(), name='sc_daily_sales'),
    path('bp/sales/day', BPDailySalesListView.as_view(), name = 'bp_daily_sales'),

]
from django.urls import path
from .views import DailySalesListView, DailySalesAnalysisView, SCDailySalesListView, BPDailySalesListView, NaverSearchingListView

app_name = 'store'
urlpatterns =[
    path('sales/day', DailySalesListView.as_view(), name='daily_sales_list'),
    path('sales/analysis', DailySalesAnalysisView.as_view(), name='sales_analysis'),
    path('blog', NaverSearchingListView.as_view(), name='naver_blog_list'),

    path('sc/sales/day', SCDailySalesListView.as_view(), name='sc_daily_sales'),
    path('bp/sales/day', BPDailySalesListView.as_view(), name = 'bp_daily_sales'),

]
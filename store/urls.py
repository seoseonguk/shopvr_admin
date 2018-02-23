from django.urls import path
from .views import TimeSalesListView

app_name = 'store'
urlpatterns =[
    path('sales/<str:store>', TimeSalesListView.as_view()),
]
from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:id>', views.order_detail, name='order_detail'),
    path('new/', views.post_new, name='order_new')
]
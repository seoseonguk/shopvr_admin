from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:id>', views.order_detail, name='order_detail'),
    path('new/', views.post_new, name='order_new'),
    path('item/', views.ItemListView.as_view(), name='item_list'),
    path('test/', views.test, name='test'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/new', views.ItemCreateView.as_view(), name='item_new')
]
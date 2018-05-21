from django.urls import path
from .views import franchise_hp_view, franchise_email

app_name='franchise_hp'
urlpatterns = [
    path('', franchise_hp_view, name='main'),
    path('email/',franchise_email, name='email')

]
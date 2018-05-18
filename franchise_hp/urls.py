from django.urls import path
from .views import franchise_hp_view, franchise_email

app_name='franchise_hp'
urlpatterns = [
    path('', franchise_hp_view),
    path('email/',franchise_email, name='email')

]
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, name='login', kwargs={'template_name':'accounts/login_form.html'}),
    path('logout/', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),

]
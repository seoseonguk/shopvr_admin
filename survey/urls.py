from django.urls import path
from .views import SurveyCreateView

app_name = 'survey'
urlpatterns =[
    path('<str:store>/new', SurveyCreateView.as_view()),
]
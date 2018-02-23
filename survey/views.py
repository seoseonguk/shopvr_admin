from django.shortcuts import render


from django.views.generic import CreateView
from .models import Survey, Answer

class SurveyCreateView(CreateView):
    model = Survey
    fields = '__all__'


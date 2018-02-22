from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    store = forms.CharField()
    position = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            store = self.cleaned_data['store'],
            position = self.cleaned_data['position']
        )
        return user


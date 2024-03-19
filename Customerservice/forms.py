# consumer_services/forms.py
from django import forms
from .models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']
from django import forms
from .models import PhotoEntry
class PhotoEntryForm(forms.ModelForm):
    class Meta:
        model=PhotoEntry
        fields=['photo','caption']

        
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

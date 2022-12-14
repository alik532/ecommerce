from dataclasses import field
from importlib.util import module_from_spec
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)

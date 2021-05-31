from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(label="email")

    labels = {
        'name': 'name',
    }

    class Meta:
        model = User
        fields = ("username", "name", "email")

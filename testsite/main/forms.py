from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegisterF(UserCreationForm):
    email = forms.EmailField(max_length=3000)

    class Meta:
        model = User
        fields = [
    'username', 'email', 'password1', 'password2'
        ]







class CreateNL(forms.Form):
    name = forms.CharField(label='Name',
    max_length=100)
    content = forms.Field(label='Content')
    check = forms.BooleanField(required=False)



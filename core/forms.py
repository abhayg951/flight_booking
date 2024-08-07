from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    username = email
    name = forms.CharField(max_length=150)
    address = forms.CharField(max_length=200)
    postal_code = forms.CharField(max_length=10)
    city = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['email', 'name', 'address', 'postal_code', 'city', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

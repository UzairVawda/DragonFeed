from django import forms
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, help_text="For user login")
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name.')
    email = forms.EmailField(max_length=300, help_text='Must be a Drexel Email.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
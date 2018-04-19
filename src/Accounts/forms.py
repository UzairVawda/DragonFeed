from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist. Please Register First.")
            if not user.check_password(password):
                raise forms.ValidationError("This password is incorrect. Please try again.")
            if not user.is_active:
                raise forms.ValidationError("This account is no longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    firstName = forms.CharField(label = 'First Name')
    lastName = forms.CharField(label = 'Last Name')
    email = forms.EmailField(label = 'Email Address')
    email2 = forms.EmailField(label = 'Confirm Email')
    password = forms.CharField(widget = forms.PasswordInput,label = 'Password')
    
    class Meta:
        model = User
        fields = [
            'firstName',
            'lastName',
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            return forms.ValidationError("Emails must match")
        return super(UserRegistrationForm, self).clean(*args, **kwargs)

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            return forms.ValidationError("Emails must match")
        return email

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
    email = forms.EmailField(label = 'Email Address')
    password = forms.CharField(widget = forms.PasswordInput, label = 'Password')
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm Password')
    
    class Meta:
        model = User
        fields = ('username','email','password', 'password2')

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")

        # if password != password2:
        #     raise forms.ValidationError(
        #         "Both Passwords must match does not match"
        #     )
        # return password
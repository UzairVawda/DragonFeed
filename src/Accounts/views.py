from .forms import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    print(request.user.is_authenticated()) 
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated()) 
        return render(request, 'index.html')
    return render(request, 'loginform.html', {'form':form, 'title':title})

def register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return render(request, 'adminpanel.html')
    context = {
        "form": form,
        "title": title
    }
    return render(request, 'registerform.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'index.html')    

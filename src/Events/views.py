from .models import Article
from .forms import SignUpForm
from django.views import generic
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

# index.html view - displays all of the articles
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'allArticles'

    def get_queryset(self):
        return Article.objects.all()

#formalEvents.html - displays all formal articles 
class FormalEventsView(generic.ListView):
    template_name = 'formalEvents.html'
    context_object_name = 'allArticles'
    
    def get_queryset(self):
        return Article.objects.all()

#informalEvents.html - displays all formal articles 
class InformalEventsView(generic.ListView):
    template_name = 'informalEvents.html'
    context_object_name = 'allArticles'
    
    def get_queryset(self):
        return Article.objects.all()
    
#details.html - displays more information for an event
class DetailView(generic.DetailView):
    template_name = 'details.html'
    model = Article

#articleform.html - allows the user to add an event
class AddEvent(CreateView):
    model = Article
    fields = '__all__'
    template_name = 'articleform.html'
    fields = ['Title', 'Orginization', 'Location', 'Description', 'Start', 'End', 'Tag', 'Link', 'Flyer']

#registration/signup.html - allows the users to signup 
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('article:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

#adminpanel.html - admin panel where the user can edit certain features
def AdminPanel(request):
    return render(request, 'adminpanel.html')
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


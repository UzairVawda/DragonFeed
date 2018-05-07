from django.views import generic
from models import Article
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

#Admin panel where the user can edit certain features
def AdminPanel(request):
    if request.user.is_authenticated():
        username = request.user.username
        print(username)
    else:
        username = request.user.username
        # return render(request, 'loginform.html', context)
        return redirect('/accounts/login')
    return render(request, 'adminpanel.html')

#Allows the user to add an event
class AddEvent(CreateView):
    model = Article
    fields = '__all__'
    template_name = 'articleform.html'
    fields = ['Title', 'Orginization', 'Location', 'Description', 'Start', 'End', 'Tag', 'Link', 'Flyer']

#User is given two options of deleting or updating an event
class EditEvent(generic.ListView):
    template_name = 'editEvent.html'
    context_object_name = 'allArticles'

    def get_queryset(self):
        return Article.objects.all()

#Allows the user to update details for an article
class ArticleUpdate(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'articleform.html'
    fields = ['Title', 'Orginization', 'Location', 'Description', 'Start', 'End', 'Tag', 'Link', 'Flyer']

#Deleting the event
class EventDelete(DeleteView):
	model = Article
	success_url = reverse_lazy('adminpanel:event-edits')

#Displays more information for an event
class DetailView(generic.DetailView):
    template_name = 'detailsAdminpanel.html'
    model = Article
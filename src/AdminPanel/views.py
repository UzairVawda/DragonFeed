from django.views import generic
from Events.models import Article
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

#adminpanel.html - admin panel where the user can edit certain features
def AdminPanel(request):
    if request.user.is_authenticated():
        username = request.user.username
        print(username)
    else:
        username = request.user.username
        # return render(request, 'loginform.html', context)
        return redirect('/accounts/login')
    return render(request, 'adminpanel.html')

#articleform.html - allows the user to add an event
class AddEvent(CreateView):
    model = Article
    fields = '__all__'
    template_name = 'articleform.html'
    fields = ['Title', 'Orginization', 'Location', 'Description', 'Start', 'End', 'Tag', 'Link', 'Flyer']

class EditEvent(generic.ListView):
    template_name = 'editEvent.html'
    context_object_name = 'allArticles'

    def get_queryset(self):
        return Article.objects.all()

class EventDelete(DeleteView):
	model = Article
	success_url = reverse_lazy('adminpanel:adminpanel')

class AlbumUpdate(UpdateView):
	model = Article
	fields = '__all__'
	template_name = 'articleform.html'
	fields = ['Title', 'Orginization', 'Location', 'Description','Start','End','Link','Tag','Flyer']


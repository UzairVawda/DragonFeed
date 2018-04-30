from . import views
from django.conf.urls import include, url

app_name = 'adminpanel'

urlpatterns = [
    #admin panel - where the user can add an event, edit a previous event, make suggestions, and logout
    url(r'^$', views.AdminPanel, name='adminpanel'),
    
    #add event - where the user can add events 
    url(r'^addevent$', views.AddEvent.as_view(), name="addevent"),

    #admin panel - where the user can add an event, edit a previous event, make suggestions, and logout
    url(r'^edits$', views.EditEvent.as_view(), name='edit-event'),

    #delete event- deletes the event
    url(r'^(?P<pk>[0-9]+)/delete/$', views.EventDelete.as_view(), name='event-delete'),

    #edit event - where the user can go to update an event
    url(r'^(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='event-update'),
]
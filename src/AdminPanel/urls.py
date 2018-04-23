from . import views
from django.conf.urls import include, url

app_name = 'adminpanel'

urlpatterns = [
    #admin panel - where the user can add an event, edit a previous event, make suggestions, and logout
    url(r'^adminpanel$', views.AdminPanel, name='adminpanel'),
]
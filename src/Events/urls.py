from . import views 
from django.conf.urls import include, url
# from django.contrib.auth import views as auth_views

app_name = 'article'

urlpatterns = [
    #index view - all events will be viewed here 
    url(r'^$', views.IndexView.as_view(), name="index"),

    #formal news - news that is orginized by a drexel orginization 
    url(r'^formal$', views.FormalEventsView.as_view(), name="formal"),

    #informal news - news that is not orginized by a drexel orginization
    url(r'^informal$', views.InformalEventsView.as_view(), name="informal"),

    #detailed view - where if the user clicks on an event they get more info
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="details"),

    #add event - where the user can add events 
    url(r'^addevent$', views.AddEvent.as_view(), name="addevent"),
 
    #sign up - where the user can go in and sign up 
    url(r'^signup$', views.SignUp, name='signup'),

    #admin panel - where the user can add an event, edit a previous event, make suggestions, and logout
    # url(r'^adminpanel$', views.AdminPanel, name='adminpanel'),

    # #log in - where users can log in  
    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    
    # #log out- where users can log out  
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

]
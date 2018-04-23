from . import views 
from django.conf.urls import include, url

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

]
from . import views 
from django.conf.urls import include, url

app_name = 'accounts'

urlpatterns = [
    #log in - where users can log in  
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.register_view, name="register"),
    
]
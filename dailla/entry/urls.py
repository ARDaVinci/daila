from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views


app_name= 'entry'

urlpatterns = [
    url(r'^bye/$' , views.ByeView.as_view() , name= 'bye'),
    url(r'^login/$' , auth_views.LoginView.as_view(template_name='entry/login.html') , name = 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]

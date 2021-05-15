from django.conf.urls import url
from . import views

app_name = 'boutique'

urlpatterns = [
    url(r'^accueil/$' , views.AccueilView.as_view() , name= 'accueil'),
]

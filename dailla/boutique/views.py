from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AccueilView(LoginRequiredMixin , TemplateView):
    login_url = '/daila/login/'
    template_name = 'boutique/accueil.html'


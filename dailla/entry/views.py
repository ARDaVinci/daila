from django.views.generic import TemplateView

class ByeView(TemplateView):
    template_name = 'entry/bye.html'

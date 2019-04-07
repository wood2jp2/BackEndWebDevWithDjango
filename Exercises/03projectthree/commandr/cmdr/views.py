from django.views.generic import TemplateView, ListView
from .models import Cmdr

# Create your views here.
class HomePageView(ListView):
    model = Cmdr
    template_name = 'home.html'
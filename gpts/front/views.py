from django.shortcuts import render
from django.views.generic import View
from .  models import period
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        periods = period.objects.get(is_active=True)
        return render(request, 'front/index.html', {'periods': periods})
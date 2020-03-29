from django.shortcuts import render
from django.views.generic import View 
from .  models import period 
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        try:
            periods = period.objects.get(is_active=True)
            return render(request, 'front/index.html', {'periods': periods})
        
        except ObjectDoesNotExist:
            
            
            return render(request, 'front/index.html' )
      
            
            
        
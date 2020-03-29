from django.shortcuts import render
from django.views.generic import View
from . forms import periodForm
from front.models import period
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userinterfacedesign/index.html')


##############################################################################
# period views


class periodCreateView(LoginRequiredMixin, CreateView):
    model = period
    form_class = periodForm
    #success_url = reverse_lazy('inventory:period_list')


class periodDetailView(LoginRequiredMixin, DetailView):
    model = period


class periodUpdateView(LoginRequiredMixin, UpdateView):
    model = period
    form_class = periodForm
    template_name_suffix = '_update_form'


class periodDeleteView(LoginRequiredMixin, DeleteView):
    model = period
    #success_url = reverse_lazy('management:employee_list')


class periodListView(LoginRequiredMixin, ListView):
    model = period
    template_name = 'inventory/period_list.html'
    period = period.objects.all()
    context = locals()
    # context['period'] = period

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'period': self.period})

    # print(period)

#######################################################################################
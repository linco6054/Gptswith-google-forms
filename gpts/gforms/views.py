from django.shortcuts import render
from django.views.generic import View
from . forms import periodForm, categoryForm
from front.models import period ,category
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


class periodListView(LoginRequiredMixin, ListView):
    model = period
    template_name = 'userinterfacedesign/period_list.html'
    period = period.objects.all()
    context = locals()
    # context['period'] = period

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'period': self.period})

    # print(period)

#######################################################################################
##############################################################################
# category views


class categoryCreateView(LoginRequiredMixin, CreateView):
    model = category
    form_class = categoryForm
    success_url = reverse_lazy('gforms:category_list')


class categoryDetailView(LoginRequiredMixin, DetailView):
    model = category


class categoryUpdateView(LoginRequiredMixin, UpdateView):
    model = category
    form_class = categoryForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('gforms:category_list')


class categoryListView(LoginRequiredMixin, ListView):
    model = category
    template_name = 'front/category_list.html'
    category = category.objects.all()
    context = locals()
    # context['category'] = category

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'category': self.category})

    # print(category)

#######################################################################################
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Unit

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('units')

class UnitList(LoginRequiredMixin, ListView):
    model = Unit
    context_object_name = 'units'

class UnitDetail(LoginRequiredMixin, DetailView):
    model = Unit
    context_object_name = 'unit'
    template_name = 'base/unit.html'

class UnitCreate(LoginRequiredMixin, CreateView):
    model = Unit
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('units')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UnitCreate, self).form_valid(form)

class UnitUpdate(LoginRequiredMixin, UpdateView):
    model = Unit
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('units')

class UnitDelete(LoginRequiredMixin, DeleteView):
    model = Unit
    context_object_name = 'unit'
    success_url = reverse_lazy('units')

    
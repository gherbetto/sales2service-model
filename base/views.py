from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Unit

class UnitList(ListView):
    model = Unit
    context_object_name = 'units'

class UnitDetail(DetailView):
    model = Unit
    context_object_name = 'unit'
    template_name = 'base/unit.html'

class UnitCreate(CreateView):
    model = Unit
    fields = '__all__'
    success_url = reverse_lazy('units')

class UnitUpdate(UpdateView):
    model = Unit
    fields = '__all__'
    success_url = reverse_lazy('units')

class UnitDelete(DeleteView):
    model = Unit
    context_object_name = 'unit'
    success_url = reverse_lazy('units')

    
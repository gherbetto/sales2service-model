from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Unit

class UnitList(ListView):
    model = Unit
    context_object_name = 'units'

class UnitDetail(DetailView):
    model = Unit
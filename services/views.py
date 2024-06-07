from django.shortcuts import render
from django.views.generic import ListView, DetailView

from services.models import Services


class ServiceListView(ListView):
    model = Services
    template_name = 'services/services.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Services
    template_name = 'services/service_detail.html'
    context_object_name = 'service'


from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from contact_us.models import ContactUs
from services.models import Services


class ServiceListView(ListView):
    model = Services
    template_name = 'services/services.html'
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['contact_us'] = ContactUs.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        search = request.POST.get('search', None)
        if search is not None:
            services = Services.objects.filter(title__icontains=search)
            contact_us = ContactUs.objects.first()
            return render(request, 'services/services.html', {
                'services': services, 'contact_us': contact_us
            })
        return Http404('کلمه ای برای جستجو وارد کنید!')


class ServiceDetailView(DetailView):
    model = Services
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['contact_us'] = ContactUs.objects.first()
        return context


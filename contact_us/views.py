from django.shortcuts import render, redirect
from django.views.generic import View

from contact_us.forms import ContactForm
from contact_us.models import ContactUs


class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        contact_us = ContactUs.objects.first()
        return render(request, 'contact_us/contact_us.html', {
            'contact_form': contact_form, 'contact_us': contact_us
        })

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
        return redirect('contact_us')

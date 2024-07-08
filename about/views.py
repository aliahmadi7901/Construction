from django.shortcuts import render
from django.views.generic import View

from about.models import SiteSetting, TeamMembers
from contact_us.models import ContactUs
from home.models import HappyCustomers


class AboutUs(View):
    def get(self, request, *args, **kwargs):
        site_setting: SiteSetting = SiteSetting.objects.first()
        contact_us = ContactUs.objects.first()
        team = TeamMembers.objects.all()[:4]
        customers = HappyCustomers.objects.all()[:4]
        return render(request, 'about/about.html', {
            'site_setting': site_setting, 'contact_us': contact_us, 'team': team, 'customers': customers
        })

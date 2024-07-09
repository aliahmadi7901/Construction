from django.shortcuts import render
from django.views.generic import View

from about.models import SiteSetting, TeamMembers
from blog.models import Blog
from contact_us.models import ContactUs
from home.models import HappyCustomers
from projects.models import Project
from services.models import Services


class HeaderView(View):
    def get(self, request, *args, **kwargs):
        contact_us = ContactUs.objects.first()
        site_setting = SiteSetting.objects.first()
        return render(request, 'shared/header_component.html', {
            'contact_us': contact_us, 'site_setting': site_setting
        })


def footer_component(request):
    return render(request, 'shared/footer_component.html')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        site_setting: SiteSetting = SiteSetting.objects.first()
        contact_us = ContactUs.objects.first()
        services = Services.objects.all()[:3]
        projects = Project.objects.order_by('-id')[:4]
        team = TeamMembers.objects.all()[:4]
        customers = HappyCustomers.objects.order_by('-id')[:4]
        blogs = Blog.objects.order_by('-id')[:2]
        return render(request, 'home/home.html', {
            'site_setting': site_setting, 'contact_us': contact_us, 'services': services, 'projects': projects,
            'team': team, 'customers': customers, 'blogs': blogs
        })

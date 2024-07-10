from django.contrib import admin

from home.models import HappyCustomers, FooterLinksCategory, FooterLink


@admin.register(HappyCustomers)
class HappyCustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


@admin.register(FooterLinksCategory)
class FooterLinksCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

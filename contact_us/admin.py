from django.contrib import admin

from contact_us.models import ContactUs, Contact


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone', 'instagram')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'checked')
    list_filter = ('checked',)

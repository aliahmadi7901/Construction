from django.contrib import admin

from contact_us.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone', 'instagram')

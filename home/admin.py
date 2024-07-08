from django.contrib import admin

from home.models import HappyCustomers


@admin.register(HappyCustomers)
class HappyCustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

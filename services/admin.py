from django.contrib import admin

from services.models import Services


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title', 'short_description')
    list_filter = ('title', )


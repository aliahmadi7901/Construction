from django.contrib import admin

from about.models import SiteSetting, TeamMembers


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('project_success_count', 'rebuilding_count', 'zero_to_hundred_count')


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill')

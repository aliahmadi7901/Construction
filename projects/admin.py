from django.contrib import admin

from projects.models import ProjectGallery, ProjectCategory, Project


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'customer_name')
    list_filter = ('project_category__title',)
    search_fields = ('title', 'customer_name', 'project_type')
    inlines = (ProjectGalleryInline,)

from django.contrib import admin

from blog.models import BlogCategories, Blog, BlogComment


@admin.register(BlogCategories)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_time', 'short_descriptions')
    list_filter = ('category__title',)
    search_fields = ('title', 'short_description')


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'comment')

from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Project, ProjectCategory


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    paginate_by = 4

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.kwargs.get('category')
        if category:
            queryset = queryset.filter(project_category__title=category)
            return queryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProjectCategory.objects.all()
        return context

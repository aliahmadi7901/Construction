from django.shortcuts import render
from django.views.generic import ListView, DetailView

from projects.models import Project, ProjectCategory, ProjectGallery


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        queryset = Project.objects.order_by('-id')
        category = self.kwargs.get('category')
        if category:
            queryset = queryset.filter(project_category__title=category)
            return queryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProjectCategory.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = ProjectGallery.objects.filter(project=self.get_object())
        return context

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from blog.forms import BlogCommentForm
from blog.models import Blog, BlogCategories, BlogComment


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 4
    template_name = 'blog/blogs.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['blog_category'] = BlogCategories.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.kwargs.get('category_title')
        if category_title:
            queryset = queryset.filter(category__title__icontains=category_title)
        return queryset


class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = BlogCommentForm()
        context['latest_blog'] = Blog.objects.order_by('-id')[:3]
        context['categories'] = BlogCategories.objects.all()
        current_blog = Blog.objects.get(pk=self.kwargs['pk'])
        blog_comments = BlogComment.objects.filter(is_active=True, parent=None, blog=current_blog)
        context['blog_comments_count'] = blog_comments.count()
        context['blog_comments'] = blog_comments
        return context

    def post(self, request, *args, **kwargs):
        blog_form = BlogCommentForm(self.request.POST)
        current_blog = Blog.objects.get(pk=self.kwargs['pk'])
        if blog_form.is_valid():
            BlogComment.objects.create(
                name=blog_form.cleaned_data.get('name'), email=blog_form.cleaned_data.get('email'),
                comment=blog_form.cleaned_data.get('comment'), blog=current_blog,
                parent_id=blog_form.cleaned_data.get('parent', None)
            )
        return redirect("blog_detail", pk=current_blog.id)

from django.urls import path

from projects import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='projects_page'),
    path('cat/<str:category>/', views.ProjectListView.as_view(), name='projects_category_page'),
    path('project-detail/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail_page'),
]

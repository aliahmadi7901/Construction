from django.urls import path

from projects import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='projects_page'),
    path('/<str:category>/', views.ProjectListView.as_view(), name='projects_category_page'),
]

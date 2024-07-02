from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('category/<str:category_title>/', views.BlogListView.as_view(), name='blog_category'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail')
]

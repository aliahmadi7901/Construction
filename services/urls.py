from django.urls import path

from services import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='services_page'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail_page'),
]

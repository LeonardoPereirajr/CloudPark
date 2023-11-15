from . import views
from django.urls import path

urlpatterns = [    
    path('api/v1/customer/', views.customer_api),
    path('api/v1/customer/<int:id>/', views.customer_api),
    ]
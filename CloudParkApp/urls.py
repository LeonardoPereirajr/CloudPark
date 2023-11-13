from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/customer/', views.customer_api),
    path('api/v1/customer/<int:id>/', views.customer_api),
    
    path('api/v1/vehicle/', views.vehicle_api),
    path('api/v1/vehicle/<int:id>/', views.vehicle_api),

    
]
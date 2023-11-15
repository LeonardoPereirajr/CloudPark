from django.urls import path
from . import views

urlpatterns = [
  
    path('api/v1/vehicle/', views.vehicle_api),
    path('api/v1/vehicle/<int:id>/', views.vehicle_api),
    
 
]
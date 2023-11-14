from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/customer/', views.customer_api),
    path('api/v1/customer/<int:id>/', views.customer_api),
    
    path('api/v1/plan/', views.plan_api),
    path('api/v1/plan/<int:id>/', views.plan_api),
   
    path('api/v1/vehicle/', views.vehicle_api),
    path('api/v1/vehicle/<int:id>/', views.vehicle_api),

    path('api/v1/contract/', views.contract_api),
    path('api/v1/contract/<int:id>/', views.contract_api),
    
    path('api/v1/customerplan/', views.customer_plan_api),
    path('api/v1/customerplan/<int:id>/', views.customer_plan_api),

    path('api/v1/parkmovement/', views.park_movement_api),
    path('api/v1/parkmovement/<int:id>/', views.park_movement_api),
    
]
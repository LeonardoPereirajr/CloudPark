from django.urls import path
from . import views

urlpatterns = [
  
    path('api/v1/customerplan/', views.customer_plan_api),
    path('api/v1/customerplan/<int:id>/', views.customer_plan_api),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/plan/', views.plan_api),
    path('api/v1/plan/<int:id>/', views.plan_api)    
]
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/contract/', views.contract_api),
    path('api/v1/contract/<int:id>/', views.contract_api)    
]
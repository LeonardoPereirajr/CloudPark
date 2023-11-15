from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/parkmovement/', views.park_movement_api),
    path('api/v1/parkmovement/<int:id>/', views.park_movement_api)    
]
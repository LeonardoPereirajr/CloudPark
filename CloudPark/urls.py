from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CloudParkApp.vehicle.urls')),
    path('', include('CloudParkApp.customer.urls')),
    path('', include('CloudParkApp.customer_plan.urls')),
    path('', include('CloudParkApp.contract.urls')),
    path('', include('CloudParkApp.plan.urls')),
    path('', include('CloudParkApp.parkmovement.urls')),
]

from django.db import models
from CloudParkApp.customer.models import Customer


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10)
    model = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=50, null=True)
    customer_id =  models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

from django.db import models
from django.shortcuts import get_object_or_404

from CloudParkApp.customer.models import Customer
from CloudParkApp.plan.models import Plan

class CustomerPlan(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True)

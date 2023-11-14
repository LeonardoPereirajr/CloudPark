from django.db import models
from django.shortcuts import get_object_or_404

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    card_id = models.CharField(max_length=10, null=True)


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10)
    model = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=50, null=True)
    customer_id =  models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

def get_vehicle_info_by_id(vehicle_id):
    try:
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        return {
            'plate': vehicle.plate,
            'customer_id': vehicle.customer_id.id if vehicle.customer_id else None
        }
    except Vehicle.DoesNotExist:
        return None

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    value = models.FloatField()

class CustomerPlan(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True)

def has_monthly_plan(customer_id):
    return CustomerPlan.objects.filter(customer_id=customer_id, plan_id__description='Mensal').exists()

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    max_value = models.FloatField(null=True)
    rules = models.ManyToManyField('ContractRule', blank=True)

def get_max_value_from_contract():
    try:
        last_rule = ContractRule.objects.order_by('-id').first()

        if last_rule:
            return last_rule.until
        else:
            return None
    except ContractRule.DoesNotExist:
        return None

class ContractRule(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    until = models.IntegerField()
    value = models.FloatField()

class ParkMovement(models.Model):
    id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    value = models.FloatField(null=True)

def calculate_parking_fee(entry_datetime, exit_datetime):
    duration_minutes = (exit_datetime - entry_datetime).total_seconds() / 60

    rule = ContractRule.objects.filter(until__gte=duration_minutes).order_by('until').first()

    if rule:
        return rule.value
    else:
        
        max_rule = ContractRule.objects.order_by('-until').first()
        return max_rule.value if max_rule else 0

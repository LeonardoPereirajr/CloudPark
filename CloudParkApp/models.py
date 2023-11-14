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

def get_plan_description_by_vehicle_id(vehicle_id):
    print(f"vehicle_id: {vehicle_id}")
    try:
        vehicle_info = get_vehicle_info_by_id(vehicle_id)

        if vehicle_info:
            customer_plan = CustomerPlan.objects.filter(customer_id=vehicle_info['customer_id']).first()
            print(f"customer_plan: {customer_plan}")
            if customer_plan:
                plan_id = customer_plan.plan_id
                plan_description = Plan.objects.filter(id=plan_id).values('description').first()
                print(f"plan_description: {plan_description}")
                if plan_description:
                    return plan_description['description']
                else:
                    return None
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error getting plan description: {str(e)}")
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

@staticmethod
def get_rotative_contract():
        try:
            return Contract.objects.get(description='Contrato Rotativo')
        except Contract.DoesNotExist:
            return Contract.objects.create(description='Contrato Rotativo', max_value=0.0)

def calculate_value_based_on_rules(self, duration_minutes):
        rules = self.contractrule_set.order_by('until')

        total_value = 0.0
        remaining_duration = duration_minutes

        for rule in rules:
            if remaining_duration <= rule.until:
                total_value += remaining_duration * rule.value
                break
            else:
                total_value += rule.until * rule.value
                remaining_duration -= rule.until

        return min(total_value, self.max_value)


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

def calculate_parking_fee(entry_datetime, exit_datetime, contract_rules):
    duration_minutes = (exit_datetime - entry_datetime).total_seconds() / 60
    total_fee = 0.0

    for rule in contract_rules:
        if duration_minutes <= rule['until']:
            total_fee = rule['value']
            break

    return total_fee

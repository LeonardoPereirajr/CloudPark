from rest_framework import serializers
from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'card_id')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate', 'model', 'description', 'customer_id')

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'description', 'value')

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPlan
        fields = ('id', 'customer_id', 'plan_id', 'due_date')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'description', 'max_value')

class ContractRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractRule
        fields = ('id', 'contract_id', 'until', 'value')

class ParkMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkMovement
        fields = ('id', 'entry_date', 'exit_date', 'vehicle_id', 'value')
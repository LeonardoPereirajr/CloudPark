from CloudParkApp.customer_plan.models import CustomerPlan
from rest_framework import serializers

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPlan
        fields = ('id', 'customer_id', 'plan_id', 'due_date')

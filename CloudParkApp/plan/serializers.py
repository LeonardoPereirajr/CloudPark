from rest_framework import serializers
from CloudParkApp.plan.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'description', 'value')

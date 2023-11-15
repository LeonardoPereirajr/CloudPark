from rest_framework import serializers
from CloudParkApp.contract.models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'description', 'max_value')

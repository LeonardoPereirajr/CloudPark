from rest_framework import serializers

from CloudParkApp.contract_rule.models import ContractRule

class ContractRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractRule
        fields = ('id', 'contract_id', 'until', 'value')

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CloudParkApp.contract_rule.models import ContractRule

from CloudParkApp.contract_rule.serializers import ContractRuleSerializer

from django.views.decorators.csrf import csrf_exempt
from .models import Contract
from .serializers import (
    ContractSerializer,
)

@csrf_exempt
def contract_api(request, id=None):
    if request.method == 'GET':
        contracts = Contract.objects.all()
        contract_serializer = ContractSerializer(contracts, many=True)
        return JsonResponse(contract_serializer.data, safe=False)

    elif request.method == 'POST':
        contract_data = JSONParser().parse(request)
        contract_rules_data = contract_data.pop('contract_rules', [])  

        contract_serializer = ContractSerializer(data=contract_data)
        if contract_serializer.is_valid():
            contract = contract_serializer.save()

            for rule_data in contract_rules_data:
                rule_data['contract_id'] = contract.id  
                rule_serializer = ContractRuleSerializer(data=rule_data)
                if rule_serializer.is_valid():
                    rule_serializer.save()

            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        try:
            contract = Contract.objects.get(id=id)
        except Contract.DoesNotExist:
            return JsonResponse("Contract not found.", status=404)

        contract_data = JSONParser().parse(request)
        contract_rules_data = contract_data.pop('contract_rules', [])  

        contract_serializer = ContractSerializer(contract, data=contract_data)
        if contract_serializer.is_valid():
            contract_serializer.save()

            for rule_data in contract_rules_data:
                rule_data['contract_id'] = contract.id
                rule_id = rule_data.pop('id', None)
                if rule_id:
                    rule = ContractRule.objects.get(id=rule_id)
                    rule_serializer = ContractRuleSerializer(rule, data=rule_data)
                else:
                    rule_serializer = ContractRuleSerializer(data=rule_data)

                if rule_serializer.is_valid():
                    rule_serializer.save()

            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        try:
            contract = Contract.objects.get(id=id)
        except Contract.DoesNotExist:
            return JsonResponse("Contract not found.", status=404)

        contract.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

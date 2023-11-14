from datetime import datetime, timedelta
import json

from django.http import HttpResponseBadRequest
from .models import ContractRule, calculate_parking_fee, get_plan_description_by_vehicle_id, get_rotative_contract, get_vehicle_info_by_id, has_monthly_plan
from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import Q
from django.utils.dateparse import parse_datetime

from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement, calculate_value_based_on_rules
from .serializers import (
    CustomerSerializer,
    VehicleSerializer,
    PlanSerializer,
    CustomerPlanSerializer,
    ContractSerializer,
    ContractRuleSerializer,
    ParkMovementSerializer,
)

@csrf_exempt
def customer_api(request, id=0):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customer_serializer.data, safe=False)

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        existing_customer_name = Customer.objects.filter(name=customer_data['name']).first()
        if existing_customer_name:
            return JsonResponse("Customer with the same name already exists.", status=400)

        card_id = customer_data.get('card_id')
        if card_id:
            existing_customer_card = Customer.objects.filter(card_id=card_id).first()
            if existing_customer_card:
                return JsonResponse("Customer with the same card ID already exists.", status=400)

        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer = Customer.objects.get(id=customer_data['id'])
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        customer = Customer.objects.get(id=id)
        customer.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def vehicle_api(request, id=0):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        vehicle_serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(vehicle_serializer.data, safe=False)

    elif request.method == 'POST':
        vehicle_data = JSONParser().parse(request)
        plate = vehicle_data.get('plate')

        existing_vehicle = Vehicle.objects.filter(plate=plate).first()

        if existing_vehicle:
            if existing_vehicle.customer_id is None:
                vehicle_serializer = VehicleSerializer(existing_vehicle, data=vehicle_data)
                if vehicle_serializer.is_valid():
                    vehicle_serializer.save()
                    return JsonResponse("Added Successfully!!", safe=False)
                return JsonResponse("Failed to Add.", safe=False)
            else:
                return JsonResponse("Vehicle already linked to a customer.", safe=False)
        else:

            vehicle_serializer = VehicleSerializer(data=vehicle_data)
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
                return JsonResponse("Added Successfully!!", safe=False)
            return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        vehicle_data = JSONParser().parse(request)
        vehicle = Vehicle.objects.get(id=vehicle_data['id'])
        vehicle_serializer = VehicleSerializer(vehicle, data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        vehicle = Vehicle.objects.get(id=id)
        vehicle.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def plan_api(request, id=0):
    if request.method == 'GET':
        plans = Plan.objects.all()
        plan_serializer = PlanSerializer(plans, many=True)
        return JsonResponse(plan_serializer.data, safe=False)

    elif request.method == 'POST':
        plan_data = JSONParser().parse(request)
        plan_serializer = PlanSerializer(data=plan_data)
        if plan_serializer.is_valid():
            plan_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        plan_data = JSONParser().parse(request)
        plan = Plan.objects.get(id=plan_data['id'])
        plan_serializer = PlanSerializer(plan, data=plan_data)
        if plan_serializer.is_valid():
            plan_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        plan = Plan.objects.get(id=id)
        plan.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def customer_plan_api(request, id=0):
    if request.method == 'GET':
        customer_plans = CustomerPlan.objects.all()
        customer_plan_serializer = CustomerPlanSerializer(customer_plans, many=True)
        return JsonResponse(customer_plan_serializer.data, safe=False)

    elif request.method == 'POST':
        customer_plan_data = JSONParser().parse(request)
        existing_customer_plan = CustomerPlan.objects.filter(
            customer_id=customer_plan_data['customer_id'],
            plan_id=customer_plan_data['plan_id']
        ).first()

        if existing_customer_plan:
            return JsonResponse("CustomerPlan already exists.", safe=False)

        customer_plan_serializer = CustomerPlanSerializer(data=customer_plan_data)
        if customer_plan_serializer.is_valid():
            customer_plan_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        customer_plan_data = JSONParser().parse(request)
        customer_plan = CustomerPlan.objects.get(id=customer_plan_data['id'])
        customer_plan_serializer = CustomerPlanSerializer(customer_plan, data=customer_plan_data)
        if customer_plan_serializer.is_valid():
            customer_plan_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        customer_plan = CustomerPlan.objects.get(id=id)
        customer_plan.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

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

@csrf_exempt
def park_movement_api(request, id=0):
    if request.method == 'GET':
        movements = ParkMovement.objects.all()
        movement_serializer = ParkMovementSerializer(movements, many=True)
        return JsonResponse(movement_serializer.data, safe=False)
       
    if request.method == 'POST':
        try:
            park_data = json.loads(request.body.decode('utf-8'))
            entry_date = parse_datetime(park_data['entry_date'])
            exit_date = parse_datetime(park_data['exit_date']) if park_data['exit_date'] else None
            vehicle_id = int(park_data['vehicle_id'])

            existing_movement = ParkMovement.objects.filter(vehicle_id=vehicle_id, exit_date__isnull=True).first()

            if exit_date:
                if existing_movement:
                    existing_movement.exit_date = exit_date
                    existing_movement.save()

                    value = calculate_parking_fee(existing_movement.entry_date, exit_date)
                    vehicle_info = get_vehicle_info_by_id(vehicle_id)
                    monthly_payer = has_monthly_plan(vehicle_info['customer_id'])
                    return JsonResponse({
                        "message": "Exit Registered",
                        "customer_id": vehicle_info['customer_id'],
                        "plate": vehicle_info['plate'],
                        "monthlyPayer": monthly_payer,
                        "value": value
                    }, status=200)
                else:
                    return JsonResponse({"error": "Vehicle not found in the parking lot"}, status=404)
            else:
                if existing_movement:
                    return JsonResponse({"error": "Vehicle is already in the parking lot"}, status=400)
                else:
                    vehicle = Vehicle.objects.get(id=vehicle_id)

                    park_movement = ParkMovement.objects.create(entry_date=entry_date, vehicle_id=vehicle, value=0)

                    vehicle_info = get_vehicle_info_by_id(vehicle_id)
                    monthly_payer = has_monthly_plan(vehicle_info['customer_id'])
                    
                    
                    if not monthly_payer:
                        exit_date = entry_date
                        value = calculate_parking_fee(entry_date, exit_date)
                    
                    return JsonResponse({
                        "message": "Entry Registered",
                        "customer_id": vehicle_info['customer_id'],
                        "plate": vehicle_info['plate'],
                        "monthlyPayer": monthly_payer,
                        "value": value
                    }, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

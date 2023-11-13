from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement
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
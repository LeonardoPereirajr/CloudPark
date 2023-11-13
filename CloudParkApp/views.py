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

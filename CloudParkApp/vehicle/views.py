from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Vehicle
from .serializers import (
    VehicleSerializer
)

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

import json
from django.utils.timezone import now

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.utils.dateparse import parse_datetime

from CloudParkApp.contract.models import Contract
from CloudParkApp.customer.models import Customer

from CloudParkApp.services.contract_service import calculate_parking_fee, get_max_value_from_contract, has_monthly_plan
from CloudParkApp.services.vehicle_service import get_vehicle_info_by_id

from .models import Vehicle, ParkMovement
from .serializers import (
    ParkMovementSerializer,
)


@csrf_exempt
def park_movement_api(request, id=0):
    if request.method == 'GET':
        movements = ParkMovement.objects.all()
        movement_serializer = ParkMovementSerializer(movements, many=True)

        result_data = []
        for movement in movement_serializer.data:
            entry_date = parse_datetime(movement['entry_date'])
            exit_date = parse_datetime(movement['exit_date']) if movement['exit_date'] else now()

            vehicle_id = movement['vehicle_id']
            vehicle_info = get_vehicle_info_by_id(vehicle_id)
            monthly_payer = has_monthly_plan(vehicle_info['customer_id'])

            time_difference = (exit_date - entry_date).total_seconds() / 60

            vehicle_contract_max_minutes = get_max_value_from_contract()

            value = 0

            if not monthly_payer:    
                if time_difference > vehicle_contract_max_minutes:
                    contract = Contract.objects.first()  
                    if contract:
                        value = contract.max_value
                else:
                    value = calculate_parking_fee(entry_date, exit_date)

            movement['value'] = value
            result_data.append(movement)

        return JsonResponse(result_data, safe=False)
       
    if request.method == 'POST':
        try:
            park_data = json.loads(request.body.decode('utf-8'))
            entry_date = parse_datetime(park_data['entry_date'])
            exit_date = parse_datetime(park_data['exit_date']) if park_data['exit_date'] else None
            vehicle_id = int(park_data['vehicle_id'])

            existing_movement = ParkMovement.objects.filter(vehicle_id=vehicle_id, exit_date__isnull=True).first()

            value = 0
            monthly_payer = False
            card_id = park_data.get('card_id', None)
            vehicle_contract_max_minutes = get_max_value_from_contract()
            print(f"vehicle_contract_max_minutes: {vehicle_contract_max_minutes}")
            if card_id:
                try:
                    customer = Customer.objects.get(card_id=card_id)

                    if ParkMovement.objects.filter(vehicle_id__customer_id=customer.id, exit_date__isnull=True).exclude(vehicle_id=vehicle_id).exists():
                        return JsonResponse({"error": "Card is already associated with a vehicle in the parking lot."}, status=400)
                    
                except Customer.DoesNotExist:
                    return JsonResponse({"error": "Invalid card_id. Vehicle entry denied."}, status=400)

            if exit_date:
                if existing_movement:
                    existing_movement.exit_date = exit_date
                    existing_movement.save()

                    vehicle_info = get_vehicle_info_by_id(vehicle_id)
                    monthly_payer = has_monthly_plan(vehicle_info['customer_id'])

                    time_difference = (exit_date - existing_movement.entry_date).total_seconds() / 60  
                    print(f"time_difference: {time_difference}")
                    if not monthly_payer:    
                        if time_difference > vehicle_contract_max_minutes:
                            contract = Contract.objects.first()  
                            if contract:
                                value = contract.max_value
                        else:
                            value = calculate_parking_fee(existing_movement.entry_date, exit_date)
                        
                    return JsonResponse({
                        "message": "Exit Registered",
                        "customer_id": vehicle_info['customer_id'],
                        "plate": vehicle_info['plate'],
                        "monthlyPayer": monthly_payer,
                        "value": value,
                        "card_id": card_id
                    }, status=200)
                else:
                    return JsonResponse({"error": "Vehicle not found in the parking lot"}, status=404)
            else:
                if existing_movement:
                    return JsonResponse({"error": "Vehicle is already in the parking lot"}, status=400)
                else:
                    if card_id:
                        if not Customer.objects.filter(card_id=card_id).exists():
                            return JsonResponse({"error": "Invalid card_id. Vehicle entry denied."}, status=400)

                    vehicle = Vehicle.objects.get(id=vehicle_id)

                    park_movement = ParkMovement.objects.create(entry_date=entry_date, vehicle_id=vehicle, value=0)

                    vehicle_info = get_vehicle_info_by_id(vehicle_id)
                    monthly_payer = has_monthly_plan(vehicle_info['customer_id'])

                    time_difference = (now() - entry_date).total_seconds() / 60 
                    if time_difference > vehicle_contract_max_minutes:
                        contract = Contract.objects.first()  
                        if contract:
                            value = contract.max_value
                    else:
                        exit_date = entry_date
                        value = calculate_parking_fee(entry_date, exit_date)
                    
                    return JsonResponse({
                        "message": "Entry Registered",
                        "customer_id": vehicle_info['customer_id'],
                        "plate": vehicle_info['plate'],
                        "monthlyPayer": monthly_payer,
                        "value": value,
                        "card_id": card_id
                    }, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
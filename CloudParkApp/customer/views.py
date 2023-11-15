from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Customer
from .serializers import (
    CustomerSerializer,
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
            return JsonResponse({"error": "Customer with the same name already exists."}, status=400)

        card_id = customer_data.get('card_id')
        if card_id:
            existing_customer_card = Customer.objects.filter(card_id=card_id).first()
            if existing_customer_card:
                return JsonResponse({"error": "Customer with the same card ID already exists."}, status=400)

        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse({"message": "Added Successfully!!"}, safe=False)
        return JsonResponse({"error": "Failed to Add."}, status=400)

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

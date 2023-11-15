

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import CustomerPlan
from .serializers import (
    CustomerPlanSerializer,
)

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

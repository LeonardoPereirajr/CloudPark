from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Plan
from .serializers import (
    PlanSerializer,
)

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

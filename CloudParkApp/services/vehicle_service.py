from django.shortcuts import get_object_or_404

from CloudParkApp.vehicle.models import Vehicle


def get_vehicle_info_by_id(vehicle_id):
    try:
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        return {
            'plate': vehicle.plate,
            'customer_id': vehicle.customer_id.id if vehicle.customer_id else None
        }
    except Vehicle.DoesNotExist:
        return None
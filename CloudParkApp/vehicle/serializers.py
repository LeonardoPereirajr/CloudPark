from rest_framework import serializers
from CloudParkApp.vehicle.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate', 'model', 'description', 'customer_id')

from rest_framework import serializers

from CloudParkApp.parkmovement.models import ParkMovement

class ParkMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkMovement
        fields = ('id', 'entry_date', 'exit_date', 'vehicle_id', 'value')
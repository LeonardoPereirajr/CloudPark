from django.db import models

from CloudParkApp.vehicle.models import Vehicle

class ParkMovement(models.Model):
    id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    value = models.FloatField(null=True)

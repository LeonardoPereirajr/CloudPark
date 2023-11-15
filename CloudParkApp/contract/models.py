from django.db import models

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    max_value = models.FloatField(null=True)
    rules = models.ManyToManyField('ContractRule', blank=True)

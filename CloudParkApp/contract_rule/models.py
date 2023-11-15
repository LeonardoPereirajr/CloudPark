from django.db import models

from CloudParkApp.contract.models import Contract

class ContractRule(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    until = models.IntegerField()
    value = models.FloatField()
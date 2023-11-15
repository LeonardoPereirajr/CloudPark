from CloudParkApp.contract_rule.models import ContractRule
from CloudParkApp.customer_plan.models import CustomerPlan

def get_max_value_from_contract():
    try:
        last_rule = ContractRule.objects.order_by('-id').first()

        if last_rule:
            return last_rule.until
        else:
            return None
    except ContractRule.DoesNotExist:
        return None
    
def has_monthly_plan(customer_id):
    return CustomerPlan.objects.filter(customer_id=customer_id, plan_id__description='Mensal').exists()

def calculate_parking_fee(entry_datetime, exit_datetime):
    duration_minutes = (exit_datetime - entry_datetime).total_seconds() / 60

    rule = ContractRule.objects.filter(until__gte=duration_minutes).order_by('until').first()

    if rule:
        return rule.value
    else:
        
        max_rule = ContractRule.objects.order_by('-until').first()
        return max_rule.value if max_rule else 0

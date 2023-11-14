# CloudPark

## Parking Management System
This project is a Parking Management System implemented using Django, a high-level Python web framework. The system provides APIs for managing customers, vehicles, plans, customer plans, contracts, and park movements.

# Models

Customer
id: AutoField (Primary Key)
name: CharField (max_length=50)
card_id: CharField (max_length=10, nullable)

Vehicle
id: AutoField (Primary Key)
plate: CharField (max_length=10)
model: CharField (max_length=30, nullable)
description: CharField (max_length=50, nullable)
customer_id: ForeignKey (Customer, on_delete=CASCADE, nullable)

Plan
id: AutoField (Primary Key)
description: CharField (max_length=50)
value: FloatField

CustomerPlan
id: AutoField (Primary Key)
customer_id: ForeignKey (Customer, on_delete=CASCADE)
plan_id: ForeignKey (Plan, on_delete=CASCADE)
due_date: DateTimeField (nullable)

Contract
id: AutoField (Primary Key)
description: CharField (max_length=50)
max_value: FloatField (nullable)
rules: ManyToManyField (ContractRule, blank=True)

ContractRule
id: AutoField (Primary Key)
contract_id: ForeignKey (Contract, on_delete=CASCADE)
until: IntegerField
value: FloatField

ParkMovement
id: AutoField (Primary Key)
entry_date: DateTimeField
exit_date: DateTimeField (nullable)
vehicle_id: ForeignKey (Vehicle, on_delete=CASCADE, nullable)
value: FloatField (nullable)

## ROUTES
Customer API
GET /api/v1/customer/: Get a list of all customers.
POST /api/v1/customer/: Add a new customer.
PUT /api/v1/customer/{id}/: Update customer details.
DELETE /api/v1/customer/{id}/: Delete a customer.

Vehicle API
GET /api/v1/vehicle/: Get a list of all vehicles.
POST /api/v1/vehicle/: Add a new vehicle.
PUT /api/v1/vehicle/{id}/: Update vehicle details.
DELETE /api/v1/vehicle/{id}/: Delete a vehicle.

Plan API
GET /api/v1/plan/: Get a list of all plans.
POST /api/v1/plan/: Add a new plan.
PUT /api/v1/plan/{id}/: Update plan details.
DELETE /api/v1/plan/{id}/: Delete a plan.

Customer Plan API
GET /api/v1/customerplan/: Get a list of all customer plans.
POST /api/v1/customerplan/: Add a new customer plan.
PUT /api/v1/customerplan/{id}/: Update customer plan details.
DELETE /api/v1/customerplan/{id}/: Delete a customer plan.

Contract API
GET /api/v1/contract/: Get a list of all contracts.
POST /api/v1/contract/: Add a new contract.
PUT /api/v1/contract/{id}/: Update contract details.
DELETE /api/v1/contract/{id}/: Delete a contract.

Park Movement API
GET /api/v1/parkmovement/: Get a list of all park movements.
POST /api/v1/parkmovement/: Register a new park movement.
PUT /api/v1/parkmovement/{id}/: Update park movement details.
DELETE /api/v1/parkmovement/{id}/: Delete a park movement.

Usage
Clone the repository: git clone <repository-url>


Install the required dependencies
Apply migrations to create the database schema: python manage.py migrate
Run the development server:python manage.py runserver
Access the API endpoints at http://localhost:8000/api/v1/.

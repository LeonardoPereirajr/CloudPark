# CloudPark

Navegador:
![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/2d1b6d4d-1e3e-4f2b-933a-8aadee3a2833)



Mobile
![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/15e331e2-cfe0-4322-a57f-3099c453b197)


## Parking Management System
This project is a Parking Management System implemented using Django, a high-level Python web framework. The system provides APIs for managing customers, vehicles, plans, customer plans, contracts, and park movements.

# Models

Customer  
| Campo    | Tipo          | Descrição                          |
|----------|---------------|------------------------------------|
| id       | AutoField     | Chave Primária                     |
| name     | CharField     | Máximo de 50 caracteres            |
| card_id  | CharField     | Máximo de 10 caracteres (nullable) |


Vehicle
| Campo        | Tipo          | Descrição                                          |
|--------------|---------------|----------------------------------------------------|
| id           | AutoField     | Chave Primária                                     |
| plate        | CharField     | Máximo de 10 caracteres                            |
| model        | CharField     | Máximo de 30 caracteres (nullable)                 |
| description  | CharField     | Máximo de 50 caracteres (nullable)                 |
| customer_id  | ForeignKey    | Chave estrangeira para Customer (CASCADE, nullable)|
 

Plan
| Campo        | Tipo          | Descrição                      |
|--------------|---------------|--------------------------------|
| id           | AutoField     | Chave Primária                 |
| description  | CharField     | Máximo de 50 caracteres        |
| value        | FloatField    |                                |


CustomerPlan
| Campo        | Tipo          | Descrição                                 |
|--------------|---------------|-------------------------------------------|
| id           | AutoField     | Chave Primária                            |
| customer_id  | ForeignKey    | Chave estrangeira para Customer (CASCADE) |
| plan_id      | ForeignKey    | Chave estrangeira para Plan (CASCADE)     |
| due_date     | DateTimeField | (nullable)                                |
 

Contract
| Campo        | Tipo               | Descrição                                           |
|--------------|-----------------------|--------------------------------------------------|
| id           | AutoField             | Chave Primária                                   |
| description  | CharField             | Máximo de 50 caracteres                          |
| max_value    | FloatField (nullable) |                                                  |
| rules        | ManyToManyField       | Muitos para Muitos com ContractRule (em branco)  |
 

ContractRule
| Campo        | Tipo          | Descrição                                 |
|--------------|---------------|-------------------------------------------|
| id           | AutoField     | Chave Primária                            |
| contract_id  | ForeignKey    | Chave estrangeira para Contract (CASCADE) |
| until        | IntegerField  |                                           |
| value        | FloatField    |                                           |


ParkMovement
| Campo        | Tipo          | Descrição                                          |
|--------------|---------------|----------------------------------------------------|
| id           | AutoField     | Chave Primária                                     |
| entry_date   | DateTimeField |                                                    |
| exit_date    | DateTimeField (nullable) |                                         |
| vehicle_id   | ForeignKey    | Chave estrangeira para Vehicle (CASCADE, nullable) |
| value        | FloatField (nullable) |                                            |
  

## ROUTES

Customer API
 - GET /api/v1/customer/: Get a list of all customers.
   ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/49adf2ed-8486-433a-9657-97983033b495)

 - POST /api/v1/customer/: Add a new customer.
   ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/e17435bd-4c88-43ba-9c00-c61b959d2d34)

 - PUT /api/v1/customer/{id}/: Update customer details.
   ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/a275d1df-3257-457d-b202-c85f26f5c4c3)

 - DELETE /api/v1/customer/{id}/: Delete a customer.
   ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/981b4ca3-5476-4a5a-9ca3-6dd3974e798e)

   
Vehicle API
- GET /api/v1/vehicle/: Get a list of all vehicles.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/046f8f9a-bed2-4224-8e55-777e8f1d99db)

- POST /api/v1/vehicle/: Add a new vehicle.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/d08a9bf2-79d1-4cf3-92d3-4b210c9a2b31)

- PUT /api/v1/vehicle/{id}/: Update vehicle details.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/834d0c91-fe26-4ad1-b365-0039c6a75366)

- DELETE /api/v1/vehicle/{id}/: Delete a vehicle.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/2b97b96a-b597-4510-bcc7-9124980e3afa)


Plan API
- GET /api/v1/plan/: Get a list of all plans.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/de02bb5d-2751-49b5-b839-117e4c6e5050)

- POST /api/v1/plan/: Add a new plan.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/f16a0107-584d-47be-b177-86bbe1fe416f)

- PUT /api/v1/plan/{id}/: Update plan details.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/baf2eb69-b1c4-4bcd-8666-6c16cf1b2b61)

- DELETE /api/v1/plan/{id}/: Delete a plan.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/d32d8561-2cbe-4d42-9447-9a7b0b1c5256)


Customer Plan API
- GET /api/v1/customerplan/: Get a list of all customer plans.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/e224e2ff-38a6-4274-acdf-f90ba7692b3f)

- POST /api/v1/customerplan/: Add a new customer plan.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/87f0ba4a-707d-476c-b4da-f7ffac1ee50c)

- PUT /api/v1/customerplan/{id}/: Update customer plan details.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/4b95420c-828e-4da2-ab01-0ade28290683)

- DELETE /api/v1/customerplan/{id}/: Delete a customer plan.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/6acdf217-68da-4056-bdb5-b42023f55860)


Contract API
- GET /api/v1/contract/: Get a list of all contracts.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/6bec18a6-64d2-4c5f-9130-e3f8ab76686d)

- POST /api/v1/contract/: Add a new contract.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/c601a40b-5910-4f2a-bc65-b6916ab7acb7)

- PUT /api/v1/contract/{id}/: Update contract details.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/7dd464e2-e2ae-40e0-86ec-77d4d78ad615)

- DELETE /api/v1/contract/{id}/: Delete a contract.
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/fbf8b441-6673-4801-ad84-1a1a3c0d6385)


Park Movement API
- GET /api/v1/parkmovement/: Get a list of all park movements.
![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/56a12e69-bdb5-4743-afaa-f2d8342c3ca7)



- POST /api/v1/parkmovement/: Register a new park movement.
  Entrada de veiculo rotativo:
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/701784b6-4675-4d51-aa61-518671156721)
  Sainda de veiculo rotativo:
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/5e5fa31f-01da-4155-9374-c98de799b3c2)
  Tentativa de entrar sendo que ja acusou entrada:
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/3ced01da-6318-41bc-b54a-62bf6f95ca06)
  Tentativa de entrar com cartão que ja esta no park
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/8d39cfaf-7b5f-46f7-a00d-8b41c1f95697)
  Saida de mensalista:
  ![image](https://github.com/LeonardoPereirajr/CloudPark/assets/30580018/a6b98481-432e-4c16-b6c8-bbd02c459f7f)


Usage
Clone the repository: git clone [<repository-url>](https://github.com/LeonardoPereirajr/CloudPark.git)  


Install the required dependencies  
Apply migrations to create the database schema: python manage.py migrate  
Run the development server:python manage.py runserver  
Access the API endpoints at http://localhost:8000/api/v1/.  

import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { ContractComponent } from './contract/contract.component';
import { AddEditContractComponent } from './contract/add-edit-contract/add-edit-contract.component';
import { ShowContractComponent } from './contract/show-contract/show-contract.component';
import { CustomerPlanComponent } from './customer_plan/customer-plan.component';
import { AddEditCustomerPlanComponent } from './customer_plan/add-edit-customer-plan/add-edit-customer-plan.component';
import { ShowCustomerPlanComponent } from './customer_plan/show-customer-plan/show-customer-plan.component';
import { CustomerComponent } from './customer/customer.component';
import { AddEditCustomerComponent } from './customer/add-edit-customer/add-edit-customer.component';
import { ShowCustomerComponent } from './customer/show-customer/show-customer.component';
import { AddComponent } from './parkmovement/add/add.component';
import { ShowComponent } from './parkmovement/show/show.component';
import { PlanComponent } from './plan/plan.component';
import { AddEditPlanComponent } from './plan/add-edit-plan/add-edit-plan.component';
import { ShowPlanComponent } from './plan/show-plan/show-plan.component';
import { VehicleComponent } from './vehicle/vehicle.component';
import { AddEditVehicleComponent } from './vehicle/add-edit-vehicle/add-edit-vehicle.component';
import { ShowVehicleComponent } from './vehicle/show-vehicle/show-vehicle.component';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { SharedService } from './shared.service';

@NgModule({
  declarations: [
    AppComponent,
    ContractComponent,
    AddEditContractComponent,
    ShowContractComponent,
    CustomerPlanComponent,
    AddEditCustomerPlanComponent,
    ShowCustomerPlanComponent,
    CustomerComponent,
    AddEditCustomerComponent,
    ShowCustomerComponent,
    AddComponent,
    ShowComponent,
    PlanComponent,
    AddEditPlanComponent,
    ShowPlanComponent,
    VehicleComponent,
    AddEditVehicleComponent,
    ShowVehicleComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }

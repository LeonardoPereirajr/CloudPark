import { RouterModule, Routes } from '@angular/router';
import { CustomerComponent } from './customer/customer.component';
import { NgModule } from '@angular/core';
import { ShowCustomerComponent } from './customer/show-customer/show-customer.component';
import { AddEditCustomerComponent } from './customer/add-edit-customer/add-edit-customer.component';
import { VehicleComponent } from './vehicle/vehicle.component';
import { ContractComponent } from './contract/contract.component';
import { PlanComponent } from './plan/plan.component';
import { ParkmovementComponent } from './parkmovement/parkmovement.component';

export const routes: Routes = [
  { path: 'customer', component: CustomerComponent },
  { path: 'vehicle', component: VehicleComponent },
  { path: 'contract', component: ContractComponent},
  { path: 'plan', component: PlanComponent},
  { path: 'parkmovement', component: ParkmovementComponent},
];

NgModule({

  declarations: [
    CustomerComponent,
    ShowCustomerComponent,
    AddEditCustomerComponent,
    VehicleComponent,
    ContractComponent,
    PlanComponent
  ],

  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

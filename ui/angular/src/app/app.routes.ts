import { RouterModule, Routes } from '@angular/router';
import { CustomerComponent } from './customer/customer.component';
import { NgModule } from '@angular/core';
import { ShowCustomerComponent } from './customer/show-customer/show-customer.component';
import { AddEditCustomerComponent } from './customer/add-edit-customer/add-edit-customer.component';
import { VehicleComponent } from './vehicle/vehicle.component';

export const routes: Routes = [
  { path: 'customer', component: CustomerComponent },
  { path: 'vehicle', component: VehicleComponent },
];

NgModule({

  declarations: [
    CustomerComponent,
    ShowCustomerComponent,
    AddEditCustomerComponent,
  ],

  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

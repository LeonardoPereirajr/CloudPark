import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CustomerComponent } from './customer/customer.component';
import { VehicleComponent } from './vehicle/vehicle.component';
import { Routes } from '@angular/router';


const routes: Routes = [
  { path: 'customer', component: CustomerComponent },
  { path: 'vehicle', component: VehicleComponent },
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ]
})
export class AppRoutingModule { }

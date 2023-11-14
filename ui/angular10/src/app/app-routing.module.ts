import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CustomerComponent } from './customer/customer.component';
import { AddEditCustomerComponent } from './customer/add-edit-customer/add-edit-customer.component';
import { ShowCustomerComponent } from './customer/show-customer/show-customer.component';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  { path: 'customer', component: CustomerComponent },
  { path: 'show-customer', component: ShowCustomerComponent},
  { path: 'add-customer', component: AddEditCustomerComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

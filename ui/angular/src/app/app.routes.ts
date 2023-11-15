import { RouterModule, Routes } from '@angular/router';
import { CustomerComponent } from './customer/customer.component';
import { NgModule } from '@angular/core';

export const routes: Routes = [
  { path: 'customer', component: CustomerComponent },
];

NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

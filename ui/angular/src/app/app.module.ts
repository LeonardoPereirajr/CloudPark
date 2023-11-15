import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AddEditCustomerComponent } from './customer/add-edit-customer/add-edit-customer.component';
import { ShowCustomerComponent } from './customer/show-customer/show-customer.component';
import { CustomerComponent } from './customer/customer.component';
import { SharedService } from './shared.service';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule,ReactiveFormsModule} from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@NgModule({
  declarations: [
    CustomerComponent,
    ShowCustomerComponent,
    AddEditCustomerComponent,
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  imports: [
    BrowserModule,
    CommonModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [SharedService],
})
export class AppModule { }

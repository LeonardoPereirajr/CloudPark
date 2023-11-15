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
import { VehicleComponent } from './vehicle/vehicle.component';
import { ShowVehicleComponent } from './vehicle/show-vehicle/show-vehicle.component';
import { AddEditVehicleComponent } from './vehicle/add-edit-vehicle/add-edit-vehicle.component';
import { ParkmovementComponent } from './parkmovement/parkmovement.component';
import { ShowParkComponent } from './parkmovement/show-park/show-park.component';
import { AddParkComponent } from './parkmovement/add-park/add-park.component';

@NgModule({
  declarations: [
    CustomerComponent,
    ShowCustomerComponent,
    AddEditCustomerComponent,
    VehicleComponent,
    ShowVehicleComponent,
    AddEditVehicleComponent,
    ParkmovementComponent,
    ShowParkComponent,
    AddParkComponent,
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
  bootstrap: [CustomerComponent]
})
export class AppModule { }

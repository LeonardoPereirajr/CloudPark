import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000";

  constructor(private http:HttpClient) { }

  getCustomers(): Observable<any[]> {
    return this.http.get<any[]>(`${this.APIUrl}/api/v1/customer/`);
  }

  getCustomerById(id: number): Observable<any> {
    return this.http.get<any>(`${this.APIUrl}/api/v1/customer/${id}/`);
  }

  addCustomer(data: any): Observable<any> {
    return this.http.post<any>(`${this.APIUrl}/api/v1/customer/`, data);
  }

  updateCustomer(data: any): Observable<any> {
    return this.http.put<any>(`${this.APIUrl}/api/v1/customer/${data.id}/`, data);
  }

  deleteCustomer(id: number): Observable<any> {
    return this.http.delete<any>(`${this.APIUrl}/api/v1/customer/${id}/`);
  }

  getPlans(): Observable<any[]> {
    return this.http.get<any[]>(`${this.APIUrl}/api/v1/plan/`);
  }

  getPlanById(id: number): Observable<any> {
    return this.http.get<any>(`${this.APIUrl}/api/v1/plan/${id}/`);
  }

  addPlan(data: any): Observable<any> {
    return this.http.post<any>(`${this.APIUrl}/api/v1/plan/`, data);
  }

  updatePlan(data: any): Observable<any> {
    return this.http.put<any>(`${this.APIUrl}/api/v1/plan/${data.id}/`, data);
  }

  deletePlan(id: number): Observable<any> {
    return this.http.delete<any>(`${this.APIUrl}/api/v1/plan/${id}/`);
  }

  getVehicles(): Observable<any[]> {
    return this.http.get<any[]>(`${this.APIUrl}/api/v1/vehicle/`);
  }

  getVehicleById(id: number): Observable<any> {
    return this.http.get<any>(`${this.APIUrl}/api/v1/vehicle/${id}/`);
  }

  addVehicle(data: any): Observable<any> {
    return this.http.post<any>(`${this.APIUrl}/api/v1/vehicle/`, data);
  }

  updateVehicle(data: any): Observable<any> {
    return this.http.put<any>(`${this.APIUrl}/api/v1/vehicle/${data.id}/`, data);
  }

  deleteVehicle(id: number): Observable<any> {
    return this.http.delete<any>(`${this.APIUrl}/api/v1/vehicle/${id}/`);
  }

  getContracts(): Observable<any[]> {
    return this.http.get<any[]>(`${this.APIUrl}/api/v1/contract/`);
  }

  getContractById(id: number): Observable<any> {
    return this.http.get<any>(`${this.APIUrl}/api/v1/contract/${id}/`);
  }

  addContract(data: any): Observable<any> {
    return this.http.post<any>(`${this.APIUrl}/api/v1/contract/`, data);
  }

  updateContract(data: any): Observable<any> {
    return this.http.put<any>(`${this.APIUrl}/api/v1/contract/${data.id}/`, data);
  }

  deleteContract(id: number): Observable<any> {
    return this.http.delete<any>(`${this.APIUrl}/api/v1/contract/${id}/`);
  }

  getCustomerPlans(): Observable<any[]> {
    return this.http.get<any[]>(`${this.APIUrl}/api/v1/customerplan/`);
  }

  getCustomerPlanById(id: number): Observable<any> {
    return this.http.get<any>(`${this.APIUrl}/api/v1/customerplan/${id}/`);
  }

  addCustomerPlan(data: any): Observable<any> {
    return this.http.post<any>(`${this.APIUrl}/api/v1/customerplan/`, data);
  }

  updateCustomerPlan(data: any): Observable<any> {
    return this.http.put<any>(`${this.APIUrl}/api/v1/customerplan/${data.id}/`, data);
  }

  deleteCustomerPlan(id: number): Observable<any> {
    return this.http.delete<any>(`${this.APIUrl}/api/v1/customerplan/${id}/`);
  }

  getParkMovements(): Observable<any[]> {
    return this.http.get<any[]>(`${this.APIUrl}/api/v1/parkmovement/`);
  }

  getParkMovementById(id: number): Observable<any> {
    return this.http.get<any>(`${this.APIUrl}/api/v1/parkmovement/${id}/`);
  }

  addParkMovement(data: any): Observable<any> {
    return this.http.post<any>(`${this.APIUrl}/api/v1/parkmovement/`, data);
  }

}

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
}

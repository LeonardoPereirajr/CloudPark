import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedService } from '../../shared.service';

@Component({
  selector: 'app-show-customer',
  templateUrl: './show-customer.component.html',
  styleUrl: './show-customer.component.css'
})
export class ShowCustomerComponent implements OnInit{

      constructor(private service: SharedService) { }

      CustomerList: any = [];

      ngOnInit(): void {
        this.refreshCustomerList();
      }

      refreshCustomerList(){
        this.service.getCustomers().subscribe(data => {
          this.CustomerList = data;
        });
      }

}

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedService } from '../../shared.service';


@Component({
  selector: 'app-show-customer',
  templateUrl: './show-customer.component.html',
  styleUrls: ['./show-customer.component.css']
})
export class ShowCustomerComponent  {

  constructor(private service: SharedService) { }

  CustomerList: any=[] ;

  ngOnInit(): void {
    this.refreshCustomerList();
  }

  refreshCustomerList() {
    this.service.getCustomers().subscribe(data => {
      this.CustomerList = data;
    });
  }
}

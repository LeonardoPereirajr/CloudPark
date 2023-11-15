import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedService } from '../../shared.service';

@Component({
  selector: 'app-show-vehicle',
  templateUrl: './show-vehicle.component.html',
  styleUrl: './show-vehicle.component.css'
})
export class ShowVehicleComponent {

  constructor(private service: SharedService) { }

  VehicleList: any=[] ;

  ngOnInit(): void {
    this.refreshVehicleList();
  }

  refreshVehicleList() {
    this.service.getVehicles().subscribe(data => {
      this.VehicleList = data;
    });
  }

}

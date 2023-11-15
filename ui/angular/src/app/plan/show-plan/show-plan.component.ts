import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedService } from '../../shared.service';

@Component({
  selector: 'app-show-plan',
  templateUrl: './show-plan.component.html',
  styleUrl: './show-plan.component.css'
})
export class ShowPlanComponent {

  constructor(private service : SharedService) { }

  PlanList: any=[] ;

  ngOnInit(): void {
    this.refreshPlanList();
  }

  refreshPlanList() {
    this.service.getPlans().subscribe(data => {
      this.PlanList = data;
    });
  }

}

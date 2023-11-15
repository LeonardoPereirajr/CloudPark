import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedService } from '../../shared.service';

@Component({
  selector: 'app-show-contract',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './show-contract.component.html',
  styleUrl: './show-contract.component.css'
})
export class ShowContractComponent {

  constructor(private service: SharedService) { }

  ContractList: any=[] ;

  ngOnInit(): void {
    this.refreshContractList();
  }

  refreshContractList() {
    this.service.getContracts().subscribe(data => {
      this.ContractList = data;
    });
  }

}

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditCustomerPlanComponent } from './add-edit-customer-plan.component';

describe('AddEditCustomerPlanComponent', () => {
  let component: AddEditCustomerPlanComponent;
  let fixture: ComponentFixture<AddEditCustomerPlanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddEditCustomerPlanComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AddEditCustomerPlanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

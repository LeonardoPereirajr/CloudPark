import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustomerPlanComponent } from './customer-plan.component';

describe('CustomerPlanComponent', () => {
  let component: CustomerPlanComponent;
  let fixture: ComponentFixture<CustomerPlanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CustomerPlanComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CustomerPlanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

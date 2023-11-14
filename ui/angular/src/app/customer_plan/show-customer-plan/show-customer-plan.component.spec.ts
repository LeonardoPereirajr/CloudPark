import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowCustomerPlanComponent } from './show-customer-plan.component';

describe('ShowCustomerPlanComponent', () => {
  let component: ShowCustomerPlanComponent;
  let fixture: ComponentFixture<ShowCustomerPlanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ShowCustomerPlanComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ShowCustomerPlanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

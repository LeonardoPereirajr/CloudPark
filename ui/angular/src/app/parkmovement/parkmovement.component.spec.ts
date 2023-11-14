import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParkmovementComponent } from './parkmovement.component';

describe('ParkmovementComponent', () => {
  let component: ParkmovementComponent;
  let fixture: ComponentFixture<ParkmovementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ParkmovementComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ParkmovementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

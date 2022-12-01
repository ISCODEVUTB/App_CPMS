import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelfProductComponent } from './self-product.component';

describe('SelfProductComponent', () => {
  let component: SelfProductComponent;
  let fixture: ComponentFixture<SelfProductComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelfProductComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SelfProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

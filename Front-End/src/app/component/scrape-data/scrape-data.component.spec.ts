import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ScrapeDataComponent } from './scrape-data.component';

describe('ScrapeDataComponent', () => {
  let component: ScrapeDataComponent;
  let fixture: ComponentFixture<ScrapeDataComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ScrapeDataComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ScrapeDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

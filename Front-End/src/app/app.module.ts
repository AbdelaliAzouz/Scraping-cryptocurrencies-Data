import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CarouselComponent } from './component/carousel/carousel.component';
import { NavbarComponent } from './component/navbar/navbar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ScrapeDataComponent } from './component/scrape-data/scrape-data.component';
import { DownloadDataComponent } from './component/download-data/download-data.component';
import { VisualizeDataComponent } from './component/visualize-data/visualize-data.component';
import { AboutComponent } from './component/about/about.component';
import { FooterComponent } from './component/footer/footer.component';
import { CardsComponent } from './component/cards/cards.component';
import { BarChartComponent } from './component/charts/bar-chart/bar-chart.component';
import { NgChartsModule } from 'ng2-charts';
  

@NgModule({
  declarations: [
    AppComponent,
    CarouselComponent,
    NavbarComponent,
    ScrapeDataComponent,
    DownloadDataComponent,
    VisualizeDataComponent,
    AboutComponent,
    FooterComponent,
    CardsComponent,
    BarChartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    NgChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

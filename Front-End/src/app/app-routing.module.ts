import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ScrapeDataComponent } from './component/scrape-data/scrape-data.component';
import { DownloadDataComponent } from './component/download-data/download-data.component';
import { VisualizeDataComponent } from './component/visualize-data/visualize-data.component';
import { AboutComponent } from './component/about/about.component';


const routes: Routes = [
  {path: 'Scrape-data', component: ScrapeDataComponent},
  {path: 'Download-data', component: DownloadDataComponent},
  {path: 'Visualize-data', component: VisualizeDataComponent},
  {path: 'About', component: AboutComponent}

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)],
    
  exports: [RouterModule]
})
export class AppRoutingModule { }

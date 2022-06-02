import { Component, OnInit } from '@angular/core';
import { NgbCarouselConfig } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.css'],
  providers: [NgbCarouselConfig]
})
export class CarouselComponent implements OnInit {


  ngOnInit(): void {
  }
  images = [
    {title: 'First Slide', short: 'First Slide Short', src: "https://www.theparliamentmagazine.eu/siteimg/share/ugc-1/fullnews/news/22531/21779_original.jpg" },
    {title: 'Second Slide', short: 'Second Slide Short', src: "https://www.forbes.com/advisor/wp-content/uploads/2021/06/top-cryptocurrencies-900x510.jpeg"},
    {title: 'Third Slide', short: 'Third Slide Short', src: "https://images.livemint.com/img/2020/12/18/600x338/bitcoin_1583349940408_1608294135162.jpg"},
    {title: 'fourth Slide', short: 'Fourth Slide Short', src: "https://www.smartcompany.com.au/wp-content/uploads/2020/12/Bitcoin.jpg"},
    {title: 'five Slide', short: 'five Slide Short', src: "https://i0.wp.com/oltnews.com/wp-content/uploads/2022/04/Crypto-Market-Plummets-Again-Top-Cryptocurrency-Prices-Today.jpg?fit=900%2C500&ssl=1"},
    {title: 'six Slide', short: 'six Slide Short', src: "https://cdn.dnaindia.com/sites/default/files/styles/half/public/2020/04/10/901440-cryptocurrency.jpg"}
  ];
  
  constructor(config: NgbCarouselConfig) {
    config.interval = 2000;
    config.keyboard = true;
    config.pauseOnHover = true;
  }

}

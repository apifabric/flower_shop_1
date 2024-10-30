import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CustomerAddress-card.component.html',
  styleUrls: ['./CustomerAddress-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CustomerAddress-card]': 'true'
  }
})

export class CustomerAddressCardComponent {


}
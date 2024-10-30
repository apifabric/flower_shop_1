import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Delivery-card.component.html',
  styleUrls: ['./Delivery-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Delivery-card]': 'true'
  }
})

export class DeliveryCardComponent {


}
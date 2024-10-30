import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Delivery-new',
  templateUrl: './Delivery-new.component.html',
  styleUrls: ['./Delivery-new.component.scss']
})
export class DeliveryNewComponent {
  @ViewChild("DeliveryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}
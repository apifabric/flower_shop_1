import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CustomerAddress-new',
  templateUrl: './CustomerAddress-new.component.html',
  styleUrls: ['./CustomerAddress-new.component.scss']
})
export class CustomerAddressNewComponent {
  @ViewChild("CustomerAddressForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}
import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DELIVERY_MODULE_DECLARATIONS, DeliveryRoutingModule} from  './Delivery-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DeliveryRoutingModule
  ],
  declarations: DELIVERY_MODULE_DECLARATIONS,
  exports: DELIVERY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DeliveryModule { }
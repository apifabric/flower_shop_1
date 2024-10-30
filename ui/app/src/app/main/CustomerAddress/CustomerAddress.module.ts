import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CUSTOMERADDRESS_MODULE_DECLARATIONS, CustomerAddressRoutingModule} from  './CustomerAddress-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CustomerAddressRoutingModule
  ],
  declarations: CUSTOMERADDRESS_MODULE_DECLARATIONS,
  exports: CUSTOMERADDRESS_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CustomerAddressModule { }
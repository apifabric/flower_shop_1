import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CustomerAddressHomeComponent } from './home/CustomerAddress-home.component';
import { CustomerAddressNewComponent } from './new/CustomerAddress-new.component';
import { CustomerAddressDetailComponent } from './detail/CustomerAddress-detail.component';

const routes: Routes = [
  {path: '', component: CustomerAddressHomeComponent},
  { path: 'new', component: CustomerAddressNewComponent },
  { path: ':id', component: CustomerAddressDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CustomerAddress-detail-permissions'
      }
    }
  }
];

export const CUSTOMERADDRESS_MODULE_DECLARATIONS = [
    CustomerAddressHomeComponent,
    CustomerAddressNewComponent,
    CustomerAddressDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CustomerAddressRoutingModule { }
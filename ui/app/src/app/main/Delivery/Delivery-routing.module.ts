import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DeliveryHomeComponent } from './home/Delivery-home.component';
import { DeliveryNewComponent } from './new/Delivery-new.component';
import { DeliveryDetailComponent } from './detail/Delivery-detail.component';

const routes: Routes = [
  {path: '', component: DeliveryHomeComponent},
  { path: 'new', component: DeliveryNewComponent },
  { path: ':id', component: DeliveryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Delivery-detail-permissions'
      }
    }
  }
];

export const DELIVERY_MODULE_DECLARATIONS = [
    DeliveryHomeComponent,
    DeliveryNewComponent,
    DeliveryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DeliveryRoutingModule { }
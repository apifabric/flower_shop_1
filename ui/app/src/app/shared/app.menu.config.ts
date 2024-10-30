import { MenuRootItem } from 'ontimize-web-ngx';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { CustomerAddressCardComponent } from './CustomerAddress-card/CustomerAddress-card.component';

import { DeliveryCardComponent } from './Delivery-card/Delivery-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { ItemCardComponent } from './Item-card/Item-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplyCardComponent } from './Supply-card/Supply-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'CustomerAddress', name: 'CUSTOMERADDRESS', icon: 'view_list', route: '/main/CustomerAddress' }
    
        ,{ id: 'Delivery', name: 'DELIVERY', icon: 'view_list', route: '/main/Delivery' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Item', name: 'ITEM', icon: 'view_list', route: '/main/Item' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'Supply', name: 'SUPPLY', icon: 'view_list', route: '/main/Supply' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CustomerCardComponent

    ,CustomerAddressCardComponent

    ,DeliveryCardComponent

    ,EmployeeCardComponent

    ,ItemCardComponent

    ,OrderCardComponent

    ,ProductCardComponent

    ,PromotionCardComponent

    ,ReviewCardComponent

    ,ScheduleCardComponent

    ,SupplierCardComponent

    ,SupplyCardComponent

];
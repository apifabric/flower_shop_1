# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 30, 2024 14:29:13
# Database: sqlite:////tmp/tmp.jUYineHx2P/flower_shop_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer in the space flower shop.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    balance = Column(Float, nullable=False)
    credit_limit = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerAddressList : Mapped[List["CustomerAddress"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Represents an employee of the flower shop.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="employee")



class Product(SAFRSBaseX, Base):
    """
    description: Represents a flower product available for sale.
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    color = Column(String)
    unit_price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="product")
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="product")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="product")



class Promotion(SAFRSBaseX, Base):
    """
    description: Represents promotional events for products.
    """
    __tablename__ = 'promotions'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    discount_percentage = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents a supplier who provides flowers.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="supplier")



class CustomerAddress(SAFRSBaseX, Base):
    """
    description: Represents the addresses of customers.
    """
    __tablename__ = 'customer_addresses'
    _s_collection_name = 'CustomerAddress'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    address_line = Column(String)
    city = Column(String)
    postal_code = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CustomerAddressList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order made by a customer.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime)
    status = Column(String)
    amount_total = Column(Float, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    DeliveryList : Mapped[List["Delivery"]] = relationship(back_populates="order")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="order")



class Review(SAFRSBaseX, Base):
    """
    description: Customer reviews for products.
    """
    __tablename__ = 'reviews'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    review_date = Column(DateTime)
    rating = Column(Integer)
    comment = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    product : Mapped["Product"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class Schedule(SAFRSBaseX, Base):
    """
    description: Represents the work schedule of employees.
    """
    __tablename__ = 'schedules'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employees.id'), nullable=False)
    day = Column(String)
    start_time = Column(String)
    end_time = Column(String)

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class Supply(SAFRSBaseX, Base):
    """
    description: Tracks the supply of products from suppliers.
    """
    __tablename__ = 'supplies'
    _s_collection_name = 'Supply'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    supply_date = Column(DateTime)
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("SupplyList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplyList"))

    # child relationships (access children)



class Delivery(SAFRSBaseX, Base):
    """
    description: Information about the delivery orders.
    """
    __tablename__ = 'deliveries'
    _s_collection_name = 'Delivery'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    delivery_date = Column(DateTime)
    status = Column(String)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("DeliveryList"))

    # child relationships (access children)



class Item(SAFRSBaseX, Base):
    """
    description: Represents an item in an order.
    """
    __tablename__ = 'items'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ItemList"))
    product : Mapped["Product"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)

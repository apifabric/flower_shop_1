# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    """description: Represents a customer in the space flower shop."""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    balance = Column(Float, nullable=False, default=0.0)
    credit_limit = Column(Float, nullable=False, default=100.0)


class Order(Base):
    """description: Represents an order made by a customer."""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=True)
    amount_total = Column(Float, nullable=False, default=0.0)


class Product(Base):
    """description: Represents a flower product available for sale."""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    category = Column(String, nullable=True)
    color = Column(String, nullable=True)
    unit_price = Column(Float, nullable=True)


class Item(Base):
    """description: Represents an item in an order."""
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    amount = Column(Float, nullable=False)


class Supplier(Base):
    """description: Represents a supplier who provides flowers."""
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    contact_info = Column(String, nullable=True)


class Supply(Base):
    """description: Tracks the supply of products from suppliers."""
    __tablename__ = 'supplies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    supply_date = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer, nullable=False)


class Employee(Base):
    """description: Represents an employee of the flower shop."""
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    role = Column(String, nullable=True)
    hire_date = Column(DateTime, nullable=True)


class Schedule(Base):
    """description: Represents the work schedule of employees."""
    __tablename__ = 'schedules'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    day = Column(String, nullable=True)
    start_time = Column(String, nullable=True)
    end_time = Column(String, nullable=True)


class Promotion(Base):
    """description: Represents promotional events for products."""
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    discount_percentage = Column(Float, nullable=False, default=0.0)


class CustomerAddress(Base):
    """description: Represents the addresses of customers."""
    __tablename__ = 'customer_addresses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    address_line = Column(String, nullable=True)
    city = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)


class Delivery(Base):
    """description: Information about the delivery orders."""
    __tablename__ = 'deliveries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    delivery_date = Column(DateTime, nullable=True)
    status = Column(String, nullable=True)


class Review(Base):
    """description: Customer reviews for products."""
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    review_date = Column(DateTime, default=datetime.utcnow)
    rating = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)


# Database setup
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=True)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data

# Customers
customer1 = Customer(name="John Doe", email="john.doe@example.com", phone="123-456-7890", balance=0.0, credit_limit=150.0)
customer2 = Customer(name="Jane Smith", email="jane.smith@example.com", phone="987-654-3210", balance=30.0, credit_limit=200.0)
session.add_all([customer1, customer2])

# Products
product1 = Product(name="Galactic Rose", category="Rose", color="Blue", unit_price=15.5)
product2 = Product(name="Astral Lily", category="Lily", color="White", unit_price=12.0)
session.add_all([product1, product2])

# Orders
order1 = Order(customer_id=1, order_date=datetime.utcnow(), status="Pending", amount_total=15.5)
session.add(order1)

# Items
item1 = Item(order_id=1, product_id=1, quantity=1, amount=15.5)
session.add(item1)

# Suppliers
supplier1 = Supplier(name="Star Flora Supplies", contact_info="contact@starflora.com")
session.add(supplier1)

# Supplies
supply1 = Supply(supplier_id=1, product_id=1, supply_date=datetime.utcnow(), quantity=100)
session.add(supply1)

# Employees
employee1 = Employee(name="Albert Newton", role="Manager", hire_date=datetime(2020, 5, 20))
session.add(employee1)

# Schedules
schedule1 = Schedule(employee_id=1, day="Monday", start_time="09:00", end_time="17:00")
session.add(schedule1)

# Promotions
promotion1 = Promotion(name="Spring Bloom", start_date=datetime(2023, 3, 1), end_date=datetime(2023, 5, 31), discount_percentage=10.0)
session.add(promotion1)

# Customer Addresses
address1 = CustomerAddress(customer_id=1, address_line="123 Space Lane", city="Lunar City", postal_code="XYZ123")
session.add(address1)

# Deliveries
delivery1 = Delivery(order_id=1, delivery_date=datetime.utcnow(), status="Scheduled")
session.add(delivery1)

# Reviews
review1 = Review(customer_id=1, product_id=1, review_date=datetime.utcnow(), rating=5, comment="Loved the space-themed roses!")
session.add(review1)

# Commit the session
session.commit()

# Close session
session.close()

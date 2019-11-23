import sqlite3
from setup_salesonhand_indexes import setup_salesonhand_indexes

conn = sqlite3.connect("CS579.db")

cursor = conn.cursor()

dropSales = 'DROP TABLE IF EXISTS Sales'
cursor.execute(dropSales)

dropSoldCars = 'DROP TABLE IF EXISTS soldCars'
cursor.execute(dropSoldCars)

dropOnHandCars = 'DROP TABLE IF EXISTS onHandCars'
cursor.execute(dropOnHandCars)

tables = []

# Create all tables here
salesTable = """CREATE TABLE Sales (
                TransactionID Integer, 
                StaffID Integer, 
                SCarVIN Integer, 
                CustomerName text, 
                CustomerPhone Integer, 
                CustomerAddress text, 
                SalePrice real
                )"""
tables.append(salesTable)

soldTable = """CREATE TABLE soldCars (
                SCarID Integer, 
                DateOfSale text
                )"""

tables.append(soldTable)

onHandTable = """CREATE TABLE onHandCars (
                OCarID Integer, 
                Availibility text
                )"""

tables.append(onHandTable)

for table in tables:
    cursor.execute(table)

conn.commit()

conn.close()

setup_salesonhand_indexes()
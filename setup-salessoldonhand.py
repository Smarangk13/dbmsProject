import sqlite3

conn = sqlite3.connect("CS579.db")

cursor = conn.cursor()

tables = []

# Create all tables here
salesTable = """CREATE TABLE Sales (
                TransactionID Integer
                StaffID Integer
                SCarVIN Integer
                CustomerName text
                CustomerPhone Integer
                CustomerAddress text
                SalePrice real
                )"""
tables.append(salesTable)

soldTable = """CREATE TABLE soldCars (
                SCarID Integer
                DateOfSale text
                )"""

tables.append(soldTable)

onHandTable = """CREATE TABLE onHandCars (
                OCarID Integer
                Availibility text
                )"""

tables.append(onHandTable)

for table in tables:
    cursor.execute(table)

conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect("CS579.db")

cursor = conn.cursor()

dropCar = 'DROP TABLE IF EXISTS Car'
cursor.execute(dropCar)

dropVendor = 'DROP TABLE IF EXISTS Vendor'
cursor.execute(dropVendor)

tables = []

# Create all tables here
carsTable = """CREATE TABLE Car (
                CarVIN Integer, 
                Model, 
                Make text, 
                Year text, 
                color text, 
                Value real, 
                Engine text, 
                VendorID Integer, 
                PurchasePrice real, 
                PurchaseDate text
                )"""
tables.append(carsTable)

vandorTable = """CREATE TABLE Vendor (
                VendorID Integer, 
                Name text text, 
                Address text, 
                PhoneNumber text, 
                VendorType text
                )"""

tables.append(vandorTable)

for table in tables:
    cursor.execute(table)

conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect("CS579.db")
cursor = conn.cursor()

SQLcommands = []

def createTable(tableName,createCommand, index = None, indexedValue = None):
    global SQLcommands
    global cursor
    dropTable = 'DROP TABLE IF EXISTS ' + tableName
    cursor.execute(dropTable)

    SQLcommands.append(createCommand)

    if index is not None:
        priceIndex = 'CREATE INDEX' + index + 'ON' + tableName+"("+indexedValue+")"
        SQLcommands.append(priceIndex)

def executeStatements():
    global
    global cursor
    global conn

    for table in SQLcommands:
        cursor.execute(table)
    conn.commit()

carsTable = """CREATE TABLE Car (
                CarVIN Integer primary key, 
                Model, 
                Make text, 
                Year text, 
                Color text, 
                Value real, 
                Engine text, 
                VendorID Integer, 
                PurchasePrice real, 
                PurchaseDate text
                )"""

vendorTable = """CREATE TABLE Vendor (
                VendorID Integer primary key, 
                Name text text, 
                Address text, 
                PhoneNumber text, 
                VendorType text
                )"""

salesTable = """CREATE TABLE Sales (
                TransactionID Integer primary key, 
                StaffID Integer, 
                SCarVIN Integer, 
                CustomerName text, 
                CustomerPhone Integer, 
                CustomerAddress text, 
                SalePrice real
                )"""

soldTable = """CREATE TABLE soldCars (
                SCarID Integer primary key, 
                DateOfSale text
                )"""

onHandTable = """CREATE TABLE onHandCars (
                OCarID Integer primary key, 
                Availibility text
                )"""

staffTable = """CREATE TABLE Staff (
                StaffID Integer primary key, 
                Name text, 
                Role text, 
                Salary real, 
                DateofEmployment text, 
                DateofBirth text, 
                Address text, 
                StaffPhone Integer
                )"""

maintenanceRecordTable = """CREATE TABLE MaintenanceRecord (
                ServiceNumber Integer primary key, 
                CarVIN Integer, 
                DateofService text, 
                Expenditure real, 
                ChargetoCustomer real, 
                NextServiceDate text
                )"""

createTable('Car',carsTable,'CostIndex','PurchasePrice')
createTable('Vendor',vendorTable)
createTable('Sales',salesTable,'SalesIndex','SalePrice')
createTable('soldCars',soldTable)
createTable('onHandCars',onHandTable)
createTable('Staff',staffTable,'PayIndex','Salary')
createTable('MaintenanceRecord',maintenanceRecordTable,'ExpenditureIndex','Expenditure')

conn.close()
import sqlite3


class setup:
    def __init__(self):
        self.conn = sqlite3.connect("CS579.db")
        self.cursor = self.conn.cursor()

        self.SQLcommands = []

    def createTable(self, tableName, createCommand, index = None, indexedValue = None):
        dropTable = 'DROP TABLE IF EXISTS ' + tableName
        self.cursor.execute(dropTable)

        self.SQLcommands.append(createCommand)

        if index is not None:
            indexCommand = 'CREATE INDEX ' + index + ' ON ' + tableName+" ("+indexedValue+")"
            self.SQLcommands.append(indexCommand)

    def executeStatements(self):
        for command in self.SQLcommands:
            # Added print to get all sql statements used(project deliverable 4)
            print(command)
            self.cursor.execute(command)
        self.conn.commit()


if __name__ == '__main__':
    dbManager = setup()
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
                    Availability text
                    )"""

    staffTable = """CREATE TABLE Staff (
                    StaffID Integer primary key, 
                    Name text, 
                    Role text, 
                    Salary real, 
                    DateOfEmployment text, 
                    DateOfBirth text, 
                    Address text, 
                    StaffPhone Integer
                    )"""

    maintenanceRecordTable = """CREATE TABLE MaintenanceRecord (
                    ServiceNumber Integer primary key, 
                    CarVIN Integer, 
                    DateOfService text, 
                    Expenditure real, 
                    ChargeToCustomer real, 
                    NextServiceDate text
                    )"""

    dbManager.createTable('Car', carsTable, 'CostIndex', 'PurchasePrice')
    dbManager.createTable('Vendor', vendorTable)
    dbManager.createTable('Sales', salesTable, 'SalesIndex', 'SalePrice')
    dbManager.createTable('soldCars', soldTable)
    dbManager.createTable('onHandCars', onHandTable)
    dbManager.createTable('Staff', staffTable, 'PayIndex', 'Salary')
    dbManager.createTable('MaintenanceRecord', maintenanceRecordTable, 'ExpenditureIndex', 'Expenditure')

    dbManager.executeStatements()
    dbManager.conn.close()

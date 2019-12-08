import sqlite3
import datetime

class dbManager:
    def __init__(self):
        self.conn = sqlite3.connect("CS579.db")
        self.cursor = self.conn.cursor()

    def addEntrySales(self, TransactionID, StaffID, SCarVIN, CustomerName, CustomerPhone, CustomerAddress, SalePrice):
        command = f"INSERT INTO Sales VALUES ({TransactionID}, {StaffID}, {SCarVIN}, '{CustomerName}', {CustomerPhone}, '{CustomerAddress}', {SalePrice});"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def addEntryCars(self, CarVIN, Model, Make, Year, Color, Value, Engine, VendorID, PurchasePrice, PurchaseDate):
        command = f"INSERT INTO Car VALUES ({CarVIN}, '{Model}', '{Make}', {Year}, '{Color}', {Value}, '{Engine}', {VendorID}, {PurchasePrice}, '{PurchaseDate}');"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def addEntryStaff(self, StaffID, Name, Role, Salary, DateofEmployment, DateofBirth, Address, StaffPhone):
        command = f"INSERT INTO Staff VALUES ({StaffID}, '{Name}', '{Role}', {Salary}, '{DateofEmployment}', '{DateofBirth}', '{Address}', {StaffPhone});"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def addEntryVendor(self, VendorID, Name, Address, PhoneNumber, VendorType):
        command = f"INSERT INTO Vendor VALUES ({VendorID}, '{Name}', '{Address}', {PhoneNumber}, '{VendorType}');"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def addEntryMaintenanceRecord(self, ServiceNumber, CarVIN, DateOfService, Expenditure, ChargeToCustomer, NextServiceDate):
        command = f"INSERT INTO MaintenanceRecord VALUES ({ServiceNumber}, {CarVIN}, '{DateOfService}', {Expenditure}, {ChargeToCustomer}, '{NextServiceDate}');"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def addEntryOnHand(self, OCarID, Availability):
        command = f"INSERT INTO onHandCars VALUES ({OCarID}, '{Availability}');"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def addEntrySold(self, SCarID, DateofSale):
        command = f"INSERT INTO soldCar VALUES ({SCarID}, '{DateofSale}');"
        print(command)
        self.cursor.execute(command)
        self.conn.commit()

    def getAllSoldCars(self):
        command = "SELECT Car.CarVIN, Car.Model, Sales.CustomerName FROM Sales JOIN Car ON Car.CarVIN = Sales.SCarVIN JOIN soldCars ON SCarID = Car.CarVIN;"
        print(command)
        self.cursor.execute(command)
        row = self.cursor.fetchone()
        print(row)
        return row

    def getTopSellingCar(self):
        command = "SELECT Model, COUNT(Model) FROM Car JOIN Sales ON Car.CarVIN = Sales.SCarVIN GROUP BY Model ORDER BY COUNT(Model);"
        print(command)
        self.cursor.execute(command)
        row = self.cursor.fetchone()
        print(row)
        return row

    # when is car x's next service date?
    def getNextService(self, CarVIN):
        command = "SELECT Car.CarVIN, NextServiceDate FROM Car JOIN MaintenanceRecord ON Car.CarVIN = MaintenanceRecord.CarVIN ORDER BY DateOfService DESC;"
        print(command)
        self.cursor.execute(command)
        row = self.cursor.fetchone()
        print(row)
        return row

    def getVehiclesUnderLimit(self, limit=20000):
        command = f"SELECT Model, Value FROM Car WHERE Value < {limit};"
        print(command)
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        return rows

    def getTopVendor(self):
        now = datetime.datetime.now()
        start = f"{now.year - 1}-01-01"
        end = f"{now.year - 1}-12-31"
        command = f"""
            SELECT Vendor.Name, COUNT(Vendor.Name) 
            FROM Sales 
            JOIN Car ON Car.CarVIN = Sales.SCarVIN 
            JOIN Vendor ON Vendor.VendorID = Car.VendorID 
            JOIN soldCars ON soldCars.SCarID = Sales.SCarVIN 
            WHERE DateOfSale BETWEEN '{start}' AND '{end}' 
            GROUP BY Vendor.Name 
            ORDER BY COUNT(Vendor.Name) DESC;
        """
        print(command)
        self.cursor.execute(command)
        row = self.cursor.fetchone()
        print(row)
        return row

if __name__ == '__main__':
    interface = dbManager()
    # interface.addEntrySales(1, 1, 1, 'Joe Johnson', 1234567890, '1 Main Street', 23000.91)
    # interface.addEntryCars(1, 'Range Rover', 'Land Rover', 2016, 'Black', 50000, 'V8', 2, 53000, '2019-11-08')
    # interface.addEntryMaintenanceRecord(1, 1, '2019-10-17', 80.0, 90.0, '2020-01-22')
    # interface.getTopSellingCar()
    # interface.getNextService(1)
    # interface.getVehiclesUnderLimit()
    interface.getAllSoldCars()

import sqlite3


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

    def getTopSellingCar(self):
        command = "SELECT Model, COUNT(Model) FROM Car JOIN Sales ON Car.CarVIN = Sales.SCarVIN GROUP BY Model ORDER BY COUNT(Model);"
        print(command)
        self.cursor.execute(command)
        row = self.cursor.fetchone()
        print(row)
        return row

if __name__ == '__main__':
    interface = dbManager()
    interface.addEntrySales(1, 1, 1, 'Joe Johnson', 1234567890, '1 Main Street', 23000.91)
    interface.addEntryCars(1, 'Range Rover', 'Land Rover', 2016, 'Black', 50000, 'V8', 2, 53000, '2019-11-08')
    interface.getTopSellingCar()

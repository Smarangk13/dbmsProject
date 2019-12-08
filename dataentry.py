from dbmsProject import dbInterface

if __name__ == '__main__':
    interface = dbInterface.dbManager()
    salesData = [(1, 1, 1, 'Joe Johnson', 1234567890, '1 Main Street', 23000.91),
                 (2,2,2, 'John '),
                 ()]
    interface.addEntrySales()
    interface.addEntryCars(1, 'Range Rover', 'Land Rover', 2016, 'Black', 50000, 'V8', 2, 53000, '2019-11-08')
    interface.ad


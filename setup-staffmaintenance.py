import sqlite3

conn = sqlite3.connect("CS579.db")

cursor = conn.cursor()

SQLcommands = []

dropStaff = 'DROP TABLE IF EXISTS Staff'
SQLcommands.append(dropStaff)

dropMaintenanceRecord = 'DROP TABLE IF EXISTS MaintenanceRecord'
SQLcommands.append(dropMaintenanceRecord)

# Create all tables here
StaffTable = """CREATE TABLE Staff (
                StaffID Integer, 
                Name text, 
                Role text, 
                Salary real, 
                DateofEmployment text, 
                DateofBirth text, 
                Address text, 
                StaffPhone Integer
                )"""
SQLcommands.append(StaffTable)
MaintenanceRecordTable = """CREATE TABLE MaintenanceRecord (
                ServiceNumber Integer, 
                CarVIN Integer, 
                DateofService text, 
                Expenditure real, 
                ChargetoCustomer real, 
                NextServiceDate text
                )"""
SQLcommands.append(MaintenanceRecordTable)

for table in SQLcommands:
    cursor.execute(table)

conn.commit()

conn.close()

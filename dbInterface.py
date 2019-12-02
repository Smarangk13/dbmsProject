import sqlite3


class dbManager:
    def __init__(self):
        conn = sqlite3.connect("CS579.db")
        self.cursor = conn.cursor()

    def addEntrySales(self, StaffID):
        # DUMMY LINE!!!
        command = "Insert into Sales " + StaffID
        print(command)
        pass


if __name__ == '__main__':
    interface = dbManager()
    interface.addEntrySales(str(205))

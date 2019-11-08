# I have my dbms project under DBMSProject, might have to chnge for yourself
#this is only a exapmple skeleton for inprovement
from DBMSProject.dbmsProject import dbInterface
class fileReader():
    def readtxt(self):
        f = open("carsdata.txt", "r")
        lines = []
        for x in f:
            print(x)
            lines.append(x)
        return lines

if __name__ == '__main__':
    reader = fileReader()
    data = reader.readtxt()
    interface = dbInterface.dbManager
    print("-----------------",data[1])
    interface.addEntrySales(interface,data[1])
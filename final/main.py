# Ahmad SLiman 1898612
import csv
import datetime#to get current date
#all my data structures
inventory = []
pastdateinv = []
damagedinv = []
types = []
pastserv = []


# Created an item class to make data manipulation easier.
class item():
    def __init__(self, id, manufacturer, type, damaged, servicedate="", price=0):
        self.id = id
        self.manufacturer = manufacturer
        self.type = type
        self.damaged = damaged
        self.servicedate = servicedate
        self.price = price

    # this is to get the different text to go in CSV files
    def print_item(self, x):
        if x == 1:
            r = self.id, self.manufacturer, self.type, self.price, self.servicedate, self.damaged
        if x == 2:
            r = self.id, self.manufacturer, self.type, self.price, self.servicedate
        return r


# The next three functions combine to make 1 full inventory data structure to make producing CSV files easier
def getManuList():
    x = 0
    with open('ManufacturerList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            id = row[0]
            manu = row[1]
            type = row[2]
            damage = row[3]
            i = item(id, manu, type, damage)
            inventory.append(i)
            l = 1
            inventory[x].print_item(l)
            x += 1


def addprice():
    with open('PriceList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x = 0
            for i in inventory:
                if inventory[x].id == row[0]:
                    inventory[x].price = row[1]
                x += 1


def addServiceDates():
    with open('ServiceDatesList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x = 0
            for i in inventory:
                if inventory[x].id == row[0]:
                    inventory[x].servicedate = row[1]
                x += 1
    y = 0
    for i in inventory:
        l = 1
        inventory[y].print_item(l)
        y += 1
#after these are run we have inventory array with all the data needed
#below begins actually producing files
def getdamaged():
    y = 0
    for i in inventory:
        if inventory[y].damaged == "damaged":
            damagedinv.append(inventory[y])
        y += 1
    x = 0
    for i in damagedinv:
        l = 2
        damagedinv[x].print_item(l)
        x += 1
    damageout() #addes all the damaged to an array

#the bellow 3 are for geting the key to sort for the files
def getKeymanu(item):
    return item.manufacturer


def getKeyprice(item):
    return item.price


def getKeyid(item):
    return item.id

#full inventory
def fullinvout():
    x = 0
    inventory.sort(key=getKeymanu)
    with open("FullInventory.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in inventory:
            l = 1
            rows = inventory[x].print_item(l)
            csvwriter.writerow(rows)
            x += 1

#damaged inventory
def damageout():
    x = 0
    damagedinv.sort(key=getKeyprice, reverse=True)
    with open("DamagedInventory.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in damagedinv:
            l = 2
            rows = damagedinv[x].print_item(l)
            csvwriter.writerow(rows)
            x += 1

#differnt type inventory
def getTypes():
    y = 0
    l = 1
    itemType = ""
    typeArray = []
    #got an array of the different item names
    for i in inventory:
        itemType = inventory[y].type
        if itemType not in types:
            types.append(itemType)
        y += 1
    #looked over invenotry to see the different types and added to files 1 by one
    for itemType in types:
        filename = itemType + "Inventory.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            x = 0
            for i in inventory:
                if inventory[x].type == itemType:
                    typeArray.append(inventory[x])
                x += 1
            typeArray.sort(key=getKeyid)
            z = 0
            for i in typeArray:
                row = typeArray[z].print_item(l)
                csvwriter.writerow(row)
                z += 1
            typeArray = []

#past service date
def datecheck():
    #I know you said no other modules but i figured this didnt count, had to get current day.
    date1 = datetime.datetime.now()
    x = 0
    #logic for seeing if its past the current date.
    for i in inventory:
        tempday = inventory[x].servicedate
        splittemp = tempday.split('/')
        servmonth = int(splittemp[0])
        servday = int(splittemp[1])
        servyear = int(splittemp[2])
        if servyear < date1.year:
            pastserv.append(inventory[x])
        elif servyear == date1.year:
            if servmonth < date1.month:
                pastserv.append(inventory[x])
            elif servmonth == date1.month:
                if servday < date1.day:
                    pastserv.append(inventory[x])
                elif servday == date1.day:
                    pastserv.append(inventory[x])
        x += 1
    y = 0
    l = 1
    #creates file
    with open("PastServiceDateInventory.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in pastserv:
            row = pastserv[y].print_item(2)
            csvwriter.writerow(row)
            y += 1


if __name__ == '__main__':
    getManuList()
    addprice()
    addServiceDates()
    getdamaged()
    fullinvout()
    getTypes()
    datecheck()

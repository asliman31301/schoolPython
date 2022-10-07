# Ahmad Sliman 1898612
from datetime import date
import sys


def main():
    # splitting current day for checks

    current = date.today()
    currentMonth = current.month
    currentDay = current.day
    currentYear = current.year

    with open("inputDates.txt") as f:
        inputdates = [line.rstrip() for line in f]
    print(inputdates)
    getUserDate(inputdates, currentMonth, currentDay, currentYear)


def getUserDate(input, currentMonth, currentDay, currentYear):
    # dictionary of months
    monthdict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    file = open("parsedDates.txt", "w")
    for x in range(len(input)):
        indate = input[x]
        if ',' in indate:
            indate2 = indate.replace(',', '')
            sliced = indate2.split(" ")
            if sliced[0] in monthdict:
                userMonth = int(monthdict[sliced[0]])
                userDay = int(sliced[1])
                userYear = int(sliced[2])
                if userYear <= currentYear:
                    if userYear == currentYear:
                        if userMonth <= currentMonth:
                            if userMonth == currentMonth:
                                if userDay <= currentDay:
                                    file.write(f'{userMonth}/{userDay}/{userYear}\n')
                                    print(f'{userMonth}/{userDay}/{userYear}')
                            else:
                                file.write(f'{userMonth}/{userDay}/{userYear}\n')
                                print(f'{userMonth}/{userDay}/{userYear}')
                        else:
                            file.write(f'{userMonth}/{userDay}/{userYear}\n')
                            print(f'{userMonth}/{userDay}/{userYear}')
                    else:
                        file.write(f'{userMonth}/{userDay}/{userYear}\n')
                        print(f'{userMonth}/{userDay}/{userYear}')


if __name__ == '__main__':
    main()

# Ahmad Sliman 1898612
from datetime import date
import sys

def main():
    formatedDate = ""

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
    # splitting current day for checks

    current = date.today()
    currentMonth = current.month
    currentDay = current.day
    currentYear = current.year


    indate = input()
    indate2 = ""
    if ',' in indate:
        indate2 = indate.replace(',', '')
    else:
        sys.exit()

    sliced = indate2.split(" ")

    if sliced[0] in monthdict:
        userMonth = monthdict[sliced[0]]
    else:
        sys.exit()
    userDay = int(sliced[1])
    userYear = int(sliced[2])

    if userYear <= currentYear and userDay <= currentDay:
        print(f'{userMonth}/{userDay}/{userYear}')

if __name__ == '__main__':
    main()

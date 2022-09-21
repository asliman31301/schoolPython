# Ahmad Sliman 1898612


def main():
    # current day vars
    month = 0
    day = 0
    year = 0
    # birthday vars
    bMonth = 0
    bDay = 0
    bYear = 0
    print("Birthday calculator")

    print("Current day")
    print("Month:", end='')
    month = int(input())
    print("Day:", end='')
    day = int(input())
    print("Year:", end='')
    year = int(input())

    print("Birthday")
    print("Month:", end='')
    bMonth = int(input())
    print("Day:", end='')
    bDay = int(input())
    print("Year:", end='')
    bYear = int(input())

    if month == bMonth and day == bDay:
        print("You are", (year - bYear), "years old.")
        print("Happy Birthday!")
    else:
        print("You are ", (year - bYear))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


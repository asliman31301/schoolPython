# Ahmad Sliman 1898612

def main():
    input_val = int(input())
    if input_val != 0:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    else:
        print("no change")

    if num_dollars == 1:
        print("1 dollar")
    elif num_dollars > 1:
        print(num_dollars, "dollars")

    if num_quarters == 1:
        print("1 quarter")
    elif num_quarters > 1:
        print(num_quarters, "quarters")

    if num_dimes == 1:
        print("1 dime")
    elif num_dimes > 1:
        print(num_dimes, "dimes")

    if num_nickels == 1:
        print("1 nickel")
    elif num_nickels > 1:
        print(num_nickels, "nickels")

    if num_pennies == 1:
        print("1 penny")
    elif num_pennies > 1:
        print(num_pennies, "pennies")


def exact_change(user_total):
    num_dollars = user_total // 100
    user_total = user_total % 100

    num_quarters = user_total // 25
    user_total = user_total % 25

    num_dimes = user_total // 10
    user_total = user_total % 10

    num_nickels = user_total // 5
    user_total = user_total % 5

    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    main()

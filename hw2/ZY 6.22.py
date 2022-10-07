#Ahmad Sliman 1898612

def main():
    #gets inputs
    xC = int(input())
    yC = int(input())
    b = int(input())
    xC2 = int(input())
    yC2 = int(input())
    b2 = int(input())
    sol = 0


    for x in range(-10, 10):
        for y in range (-10, 10):
            if (xC * x) + (yC*y) - b == 0 and (xC2 * x) + (yC2*y) - b2 == 0:
                print(x,y)
                sol = 1
                break

    if sol == 0:
        print("No solution")


if __name__ == '__main__':
    main()
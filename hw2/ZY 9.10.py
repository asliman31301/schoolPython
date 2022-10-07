# Ahmad Sliman 1898612

import csv


def main():
    filename = input()
    mylist = []
    with open(filename, 'r+') as f:
        csvf = csv.reader(f, delimiter=',')
        for lines in csvf:
            mylist = lines

    for i in range(len(mylist)):
        if mylist[i] not in mylist[:i]:
            count = 0
            for word in mylist:
                if mylist[i] == word:
                    count += 1
            print(mylist[i], count)


if __name__ == '__main__':
    main()

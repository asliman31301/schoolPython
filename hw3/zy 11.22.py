#Ahmad SLiman 1898612

if __name__ == "__main__":
    inputstr = input()
    list = inputstr.split()

    for i in range(0, len(list)):
        currentWord = list[i]
        counter = 0
        for x in range(0, len(list)):
            if list[x] == currentWord:
                counter +=1
        print(currentWord, counter)


#Ahmad SLiman 1898612

if __name__ == "__main__":
    inputstr = input()
    list = inputstr.split()

    for i in range(0, len(list)):
        list[i] = int(list[i])

    res = [ele for ele in list if ele >= 0]
    res = sorted(res)
    for i in range(len(res)):
        print(res[i], end=" ")

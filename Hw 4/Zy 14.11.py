# Ahmad Sliman 1898612


def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        minimum = i
        for j in range(len(numbers) - 1, i, -1):
            if numbers[j] > numbers[minimum]:
                minimum = j
        if minimum != i:
            numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
            #Flips the positiions by changing which number is in which postition.
        for x in range (len(numbers)):
            print(numbers[x], end=" ")
        print("")
    return numbers


if __name__ == '__main__':
    inp = input().split(" ")
    numbers = []
    for i in range(len(inp)):
        temp = int(inp[i])
        numbers.append(temp)

    selection_sort_descend_trace(numbers)

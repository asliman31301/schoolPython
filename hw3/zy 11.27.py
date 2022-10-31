
thePlayers = {}


def menu():
    userin = ''
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("")
    while(userin !='q'):
        print("Choose an option:")
        userin = str(input())
        print("")
        if(userin != 'q'):
            if(userin == 'a'):
                addplayer()
            if(userin == 'd'):
                removeplayer()
            if(userin == 'u'):
                updateplayer()
            if(userin == 'r'):
                playerabove()
            if(userin == 'o'):
                roster()




def addplayer():
    print("Enter a new player's jersey number:")
    key1 = int(input())
    print("Enter a new player's rating:")
    value1 = int(input())
    thePlayers[key1] = value1
    print()

def removeplayer():
    print("Enter a jersey number:")
    key2 = int(input())
    thePlayers.pop(key2)

def updateplayer():
    print("Enter a jersey number:")
    key3 = int(input())
    print("Enter a new rating for player:")
    value3 = int(input())
    thePlayers[key3] = value3

def playerabove():
    print("Enter a rating:")
    value4 = int(input())
    for keys in thePlayers:
        if(thePlayers[keys] > value4):
            print(f'Jersey number: {keys}, Rating: {thePlayers[keys]}')

def roster():
    print("ROSTER")
    sorted_dic = thePlayers.keys()
    sorted_dic = sorted(sorted_dic)
    for keys in sorted_dic:
        print(f'Jersey number: {keys}, Rating: {thePlayers[keys]}')
    print("")


if __name__ == '__main__':
    x = 1
    key = 0
    value = 0
    for x in range(1 ,6):
        print(f'Enter player {x}\'s jersey number:')
        key = int(input())
        print(f'Enter player {x}\'s rating:')
        value = int(input())
        thePlayers[key] = value
        print("")

    print("ROSTER")
    sorted_dict = thePlayers.keys()
    sorted_dict = sorted(sorted_dict)
    for key in sorted_dict:
        print(f'Jersey number: {key}, Rating: {thePlayers[key]}')
    print("")
    menu()
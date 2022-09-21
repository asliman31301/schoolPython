# Ahmad Sliman 1898612

# get vars
print('Enter amount of lemon juice (in cups):')
lemonj = float(input())
print("Enter amount of water (in cups):")
water = float(input())
print("Enter amount of agave nectar (in cups):")
agave = float(input())
print("How many servings does this make?")
servs = float(input())
print("")
print("Lemonade ingredients - yields", '{:.2f}'.format(servs), "servings")
print('{:.2f}'.format(lemonj), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")
print("")

# get desired amount
print("How many servings would you like to make?")
desiredServ = float(input())
print("")
diffInServings = desiredServ / servs

# cups
print("Lemonade ingredients - yields", '{:.2f}'.format(desiredServ), "servings")
print('{:.2f}'.format(lemonj * diffInServings), "cup(s) lemon juice")
print('{:.2f}'.format(water * diffInServings), "cup(s) water")
print('{:.2f}'.format(agave * diffInServings), "cup(s) agave nectar")
print("")

# Gallons
print("Lemonade ingredients - yields", '{:.2f}'.format(desiredServ), "servings")
print('{:.2f}'.format((lemonj * diffInServings)/16), "gallon(s) lemon juice")
print('{:.2f}'.format((water * diffInServings)/16), "gallon(s) water")
print('{:.2f}'.format((agave * diffInServings)/16), "gallon(s) agave nectar")


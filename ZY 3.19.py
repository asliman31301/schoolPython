#Ahmad Sliman 1898612
import math

print("Enter wall height (feet):")
h = int(input())
print("Enter wall width (feet):")
w = int(input())
area = h * w
print("Wall area:", area, "square feet")

paintNeeded = float(area/350)
print("Paint needed:", '{:.2f}'.format(paintNeeded), "gallons")
cans = math.ceil(paintNeeded)
print("Cans needed:", cans, "can(s)")
print("")

print("Choose a color to paint the wall:")
color = input()


if color == "red":
    print("Cost of purchasing red paint:",f'{"$"}{cans * 35}' )
if color == "blue":
    print("Cost of purchasing blue paint:", f'{"$"}{cans * 25}')
if color == "green":
    print("Cost of purchasing green paint:", f'{"$"}{cans * 35}')

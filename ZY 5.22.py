# Ahmad Sliman 1898612

oil = 35
tire = 19
wash = 7
wax = 12
total = 0

#menu
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")

#select services
print("Select first service:")
serv1 = input()
print("Select second service:")
serv2 = input()
print("")

#invoice
print("Davy's auto shop invoice")
print("")

if serv1 == "Oil change":
    print("Service 1: Oil change, " f'{"$"}{oil}')
    total += oil
if serv1 == "Tire rotation":
    print("Service 1: Tire rotation, " f'{"$"}{tire}')
    total += tire
if serv1 == "Car wash":
    print("Service 1: Car wash, " f'{"$"}{wash}')
    total += wash
if serv1 == "Car wax":
    print("Service 1: Car wax, " f'{"$"}{wax}')
    total += wax
if serv1 == "-":
    print("Service 1: No service")

if serv2 == "Oil change":
    print("Service 2: Oil change, " f'{"$"}{oil}')
    total += oil
if serv2 == "Tire rotation":
    print("Service 2: Tire rotation, " f'{"$"}{tire}')
    total += tire
if serv2 == "Car wash":
    print("Service 2: Car wash, " f'{"$"}{wash}')
    total += wash
if serv2 == "Car wax":
    print("Service 2: Car wax, " f'{"$"}{wax}')
    total += wax
if serv2 == "-":
    print("Service 2: No service")

print("")
print("Total:", f'{"$"}{total}')

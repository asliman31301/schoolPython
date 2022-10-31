#Ahmad SLiman 1898612

class ItemToPurchase:
    def __init__(self, name = 'none' , price = 0.0, quantity = 0):
        self.item_name = name
        self.item_price = float(price)
        self.item_quantity = quantity

    def print_item_cost(self):
        selfTot = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${selfTot}')



if __name__ == "__main__":
    print("Item 1")
    item1 = ItemToPurchase()
    print("Enter the item name:")
    item1.item_name = str(input())
    print("Enter the item price:")
    item1.item_price = int(input())
    print("Enter the item quantity:")
    item1.item_quantity = int(input())
    print("")

    print("Item 2")
    item2 = ItemToPurchase()
    print("Enter the item name:")
    item2.item_name = str(input())
    print("Enter the item price:")
    item2.item_price = int(input())
    print("Enter the item quantity:")
    item2.item_quantity = int(input())
    print("")
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print("")
    total1 = item1.item_price * item1.item_quantity
    total2 = item2.item_price * item2.item_quantity
    totalFin = total1+total2
    print(f'Total: ${totalFin}')



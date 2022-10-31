# Ahmad SLiman 1898612

class ItemToPurchase:
    def __init__(self, name='none', price=0.0, quantity=0, item_description="none"):
        self.item_name = name
        self.item_price = float(price)
        self.item_quantity = quantity
        self.item_description = item_description

    def print_item_cost(self):
        selfTot = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${selfTot}')
        return selfTot

    def print_item_description(self, item):
        print(item.item_description)


class shoppingCart:
    def __int__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        print("ADD ITEMS TO CART")
        i = ItemToPurchase()
        print("Enter the item name:")
        i.item_name = str(input())
        print("Enter the item description:")
        i.item_description = str(input())
        print("Enter the item price:")
        i.item_price = int(input())
        print("Enter the item quantity:")
        i.item_quantity = int(input())

        self.cart_items.append(i)

    def remove_item(self, item_name):
        deleted = False
        for ItemToPurchase in self.cart_items:
            counter = 0
            deleted = False
            if item_name == self.cart_items[counter].item_name:
                self.cart_items.pop(counter)
                deleted = True
                break
            else:
                counter += 1
        if deleted == False:
            print("Item not found in cart. Nothing removed.")


    def modify_item(self, item_name, q):
        mod = False
        for ItemToPurchase in self.cart_items:
            counter = 0
            mod = False
            if item_name == self.cart_items[counter].item_name:
                self.cart_items[counter].item_quantity = q
                mod = True
                break
            else:
                counter += 1
        if mod == False:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        counter = 0
        number = 0
        for ItemToPurchase in self.cart_items:
            number += self.cart_items[counter].item_quantity
            counter += 1
        return number

    def get_cost_of_cart(self):
        counter = 0
        total = 0
        for ItemToPurchase in self.cart_items:
            total += self.cart_items[counter].print_item_cost()
            counter +=1
        print("")
        print('Total: $',total)

        return total

    def print_total(self):
        if len(self.cart_items) > 0:
            print(f'{self.customer_name} Shopping cart - {self.current_date}')
            print(f'Number of items: {self.get_num_items_in_cart()}')

            self.get_cost_of_cart()
        else:
            print(f'{self.customer_name} Shopping cart - {self.current_date}')
            print(f'Number of items: {self.get_num_items_in_cart()}')
            print("")
            print("SHOPPING CART IS EMPTY")
            print("")
            print("Total: $0")
            print("")

    def print_description(self):
        counter = 0
        print(f'{self.customer_name} Shopping cart - {self.current_date}')
        print("")
        print("Item Descriptions")
        for ItemToPurchase in self.cart_items:
            print(f'{self.cart_items[counter].item_name}: {self.cart_items[counter].item_description} ')
            counter +=1
        print("")

def menu(s):
    userIn = ""
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("")

    while(userIn != "q"):
        print("Choose an option:")
        userIn = str(input())
        if userIn != 'q':
            if userIn == 'a':
                s.add_item()
            elif userIn == 'r':
                print("REMOVE ITEM FROM CART")
                print("Enter name of item to remove:")
                name = str(input())
                s.remove_item(name)
            elif userIn == 'c':
                print("CHANGE ITEM QUANTITY")
                print("Enter the item name:")
                name = str(input())
                print("Enter the new quantity:")
                q = int(input())
                s.modify_item(name, q)
            elif userIn == 'i':
                s.print_description()
            elif userIn == 'o':
                s.print_total()
        else:
            break

if __name__ == "__main__":
    s = shoppingCart()
    print("Enter customer's name:")
    s.customer_name = str(input())
    print("Enter today's date:")
    s.current_date = str(input())
    s.cart_items = []
    print("")
    print(f'Customer name: {s.customer_name}')
    print(f'Today\'s date: {s.current_date}')
    print("")

    menu(s)

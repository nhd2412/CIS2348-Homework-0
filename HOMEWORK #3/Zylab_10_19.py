# Dang Nguyen
#ID 1861688

class ItemToPurchase:
    def __init__(self, item_name= 'none', item_price=0, item_quantity=0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    def print_item_cost(self):
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity 
* self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost
    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string, end=' ')
        return string


class ShoppingCart:
    def __init__(self,customer_name= None ,current_date='January 1,2016',cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
def add_item(self,):
    print('\nADD ITEM TO CART', end='\n')

    item_name = str(input('Enter the item name:'));
    item_description = str(input('\nEnter the item description:'));
    item_price = int(input('\nEnter the item price:'));
    item_quantity = int(input('\nEnter the item quantity:\n'))

    self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))
    


def remove_item(self):
    print()
    print('REMOVE ITEM FROM CART', end='\n')
    string = str(input('Enter name of item to remove:\n'))
    i = 0
    for item in self.cart_items:
        if(item.item_name == string):               
            del self.cart_items[i]
            i += 1
            flag=True
            break
        else:
            flag=False
    if(flag==False):
        print('Item not found in cart. Nothing removed.')

def modify_item(self):
    print('\nCHANGE ITEM QUANTITY', end='\n')
    name = str(input('Enter the item name:'))       
    for item in self.cart_items:
        if(item.item_name == name):
            quantity = int(input('Enter the new quantity:'))
            item.item_quantity = quantity
            flag=True
            break
        else:
            flag=False
    if(flag==False):
        print('Item not found in cart. Nothing modified.')

def get_num_items_in_cart(self):
    num_items = 0
    for item in self.cart_items:
        num_items += item.item_quantity
    return num_items
    

def get_cost_of_cart(self):
    total_cost = 0
    cost = 0

    for item in self.cart_items:
        cost = (item.item_quantity * item.item_price)
        total_cost += cost

    return total_cost


def print_total():
   total_cost = self.get_cost_of_cart()
   if (total_cost == 0):
       print('SHOPPING CART IS EMPTY')
   else:
       output_cart()


def print_descriptions(self):
    print('OUTPUT ITEMS\' DESCRIPTIONS')
    print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date),end='\n')
    print('\nItem Descriptions', end='\n')
    for item in self.cart_items:
        print('{}: {}'.format(item.item_name, item.item_description), end='\n')
   

def output_cart(self):
    new=ShoppingCart()
    print('OUTPUT SHOPPING CART', end='\n')
    print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date),end='\n')      
    print('Number of Items:', new.get_num_items_in_cart(), end='\n\n')
    self.total_cost = self.get_cost_of_cart()
    if (self.total_cost == 0):
       print('SHOPPING CART IS EMPTY')
    else:
        pass
    tc = 0
    for item in self.cart_items:
        print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
                                         item.item_price, (item.item_quantity * item.item_price)), end='\n')
        tc += (item.item_quantity * item.item_price)
    print('\nTotal: ${}'.format(tc), end='\n')


def print_menu(new_cart):
    customer_Cart = newCart
    string=''

    menu = ('\nMENU\n'
        'a - Add item to cart\n'
        'r - Remove item from cart\n'
        'c - Change item quantity\n'
        'i - Output items\' descriptions\n'
        'o - Output shopping cart\n'
        'q - Quit\n')
    command = ''

    while(command != 'q'):
        string=''
        print('\nMENU\n'
        'a - Add item to cart\n'
        'r - Remove item from cart\n'
        'c - Change item quantity\n'
        'i - Output items\' descriptions\n'
        'o - Output shopping cart\n'
        'q - Quit\n', end='\n')

        command = input('Choose an option:')
        print()

        while(command != 'a' and command != 'o' and command != 'i' and command != 'r' and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')

    if(command == 'a'):

        customer_Cart.add_item()

    if(command == 'o'):

        customer_Cart.output_cart()

    if(command == 'i'):

        customer_Cart.print_descriptions()

    if(command == 'r'):
        customer_Cart.remove_item()
    if(command == 'c'):
        customer_Cart.modify_item()

if __name__ == "__main__":

    customer_name = str(input('Enter customer\'s name:'))
    current_date = str(input('\nEnter today\'s date:'))
    print()
    print()
    print('Customer name:', customer_name, end='\n')
    print('Today\'s date:', current_date, end='\n')
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)
'''
Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.

'''

'''
dict={ itmes   }


'''

class Restaurant:
    def __init__(self):
        self.book_table=[True]*20
        self.Menu={}
        self.cart=[]
        self.total_table=20
        
    def add_menu(self, item , price):
        self.Menu[item] = price
        print(f'{item} is added to Menu\n')
        
    def Print_Menu_Items(self):
        print('Menu                Price')
        for item , price in self.Menu.items():
            space = ' '*(20-len(item))
            print(item + space + str(price))
        print()   
        
    def is_table_available(self, table_no):
        if 0 <= table_no < self.total_table:
            return self.book_table[table_no]
        return False
        
    def table_reservation(self, table_no, customer):
        if 1 <= table_no <= self.total_table:
            table_no = table_no - 1 
            if self.is_table_available(table_no):
                print(f'Table No: {str(table_no + 1)} is reserved to Customer {customer}\n')
                self.book_table[table_no] = False
            else:
                print('Table is already reserved\n')
        else:
            print('Invalid input -> Enter Table number up to 20\n')
            
    def add_menu_to_cart(self,food , count=1):
        if food in self.Menu.keys():
            Food = [food, self.Menu[food]*count]
            self.cart.append(Food)
            print(f'{food} added to cart\n')
        else:
            print('Menu item not found\n')

    def total(self):
        total=0
        for item in self.cart:
            total = total + item[1]
        return total
            
    def customer_order(self, table, name):
        if not self.is_table_available(table - 1):
            print('-----------------')
            print(f'Customer name: {name}, Table No: {table} is reserved')
            for item in self.cart:
                print(item[0] + ' '*(20-len(item[0])) + str(item[1]))
            print()
            print('Total:'+' '*(20- len('total:')) + str(self.total()))
            print('-----------------\n')
            

        else:
            print('You are Not Reserve the table yet')
            
        

vista= Restaurant()
vista.add_menu('Pasta',100)
vista.add_menu('parotta',15)
vista.add_menu('idly',10)
vista.Print_Menu_Items()

vista.table_reservation(3 , 'Vish')


vista.add_menu_to_cart('Pasta',1)
vista.add_menu_to_cart('parotta',3)

vista.customer_order(3 ,'Vish')
vista.customer_order(2 ,'Vih')


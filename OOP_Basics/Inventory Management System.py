'''Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.

Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price'''

class Inventory:
    
    def __init__(self):
        self.inventory= {}
    
    def add_inventory(self,item_id, product , stock , price):
        row = {'Product': product , 'Stock' : stock , 'Price':price}
        self.inventory[item_id] = row
        print(f'{product} is added to inventory\n')
        
    def print_inventory(self):
        print('--------------------------')
        print('       Item Details')
        print('--------------------------')
        
        for key in self.inventory.keys():
            
            print('Item No:'+ ' '*(30- len('Item No:')) + str(key))
            print('Product Name:' + ' '*(30- len('Product Name:')) +self.inventory[key]["Product"])
            print('Stoct available:' + ' '*(30- len('Stoct available:'))+ str(self.inventory[key]["Stock"]))
            print('Price:'+ ' '*(30- len('Price:')) + str(self.inventory[key]["Price"]))
            print()
            
    def is_item(self,item):
        return item in self.inventory
    
    def update_item(self,item_id, product , stock , price): 
        if self.is_item(item_id):
            self.inventory[item_id]["Product"] =product
            self.inventory[item_id]["Stock"] = stock
            self.inventory[item_id]["rice"] = price
            print(f'Updated Item: '+ str(item_id)+ "Product: " + product+ ' \n')
            print(self.print_inventory())
        else:
            print('Item No not Exist\n')
        
        
    def Stock(self,item_no,value):
        if self.is_item(item_no):
            self.inventory[item_no]["Stock"] = value
            print(f'Updated Item no {item_no} -> Stock is Updated to {value}\n')
        else:
            print('Item No not Exist\n')
        
    def Price(self,item_no,value):
        if self.is_item(item_no):
                self.inventory[item_no]["Price"] = value
                print(f'Updated Item no {item_no} -> Price is Updated to {value}\n')
        else:
            print('Item No not Exist\n')
            
    def Product(self,item_no,value):
        if self.is_item(item_no):
            self.inventory[item_no]["Product"] = value
            print(f'Updated Item no {item_no} -> Product is Updated to {value}\n')
        else:
            print('Item No not Exist\n')

                    
viscargo = Inventory()

viscargo.add_inventory(1001 , 'Phone' , 4 , 20000)
viscargo.add_inventory(1002 , 'Mac' , 5 , 25000)
viscargo.add_inventory(1003 , 'Tab' , 2 , 27000)

viscargo.print_inventory()
'''
viscargo.Stock(1001 , 6)

viscargo.print_inventory()

viscargo.update_item(1001 , 'iphnone' , 2 , 150000)'''

viscargo.Price(1002 , 60000)

viscargo.print_inventory()




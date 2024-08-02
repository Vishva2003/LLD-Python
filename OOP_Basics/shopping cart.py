"""Write a Python program to create a class representing a shopping cart. Include methods
for adding and removing items, and calculating the total price.
"""
# list=[]
# shopping product ,price = [ : ]
# total=0

class Shopping_Cart:
    def __init__(self):
        self.items = []
              
    def list_items(self):
        if not self.items:
            print('No Item in Cart')
        
        else:
            print('Current Products       Price \n')
            for item in self.items:
                space =' '*(25 - len(item[0]))
                print(item[0] + space + str(item[1]))
                
        print('---------------------')

        
    def add_product(self,product, price):
        self.product = product
        self.price = price
        item=[self.product ,self.price]
        self.items.append(item)
        print(f'{self.product} added to your Cart \n')
        
    def remove_product(self,product):
        for item in self.items:
            if item[0].lower() == product.lower():
                self.items.remove(item)
                print(f'{product} removed from your Cart \n')
                return
        
        print('Not Found')
        
        
        
    def total(self):
        print('Selected Products       Price \n')
        for item in self.items:
            space =' '*(25 - len(item[0]))
            print(item[0] + space + str(item[1]))
        print('---------------------')
        total=0
        for item in self.items:
            total+= item[1]
        space =' '*(25 - len('Total:'))
        return f'Total:{space}{total}'
    
    
kissworks = Shopping_Cart()


kissworks.add_product('Juice',40)
kissworks.add_product('ice Cream',30)
kissworks.add_product('choco',100)

print(kissworks.list_items())

print(kissworks.remove_product('choco'))

print(kissworks.total())

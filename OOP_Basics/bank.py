'''Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
'''

class Bank:
    def __init__(self):
        self.items = {}
        
    def Create_Account(self , acc , depo):
        if depo < 1000:
            print('For a/c creation ->> minimum deposit =1000\n')
        else:
            self.items[acc] = depo
            print(f'New a/c no : {acc} is created and deposit = {depo}\n')
        
    def Customers_Details(self):
        print('<------ Customer Details ----->')
        print('  A/c No              Bal\n')
        for acc , bal in self.items.items():
            space = ' ' *(20 - len(acc))
            print('  ' +acc + space + str(bal))
        print()
            
    def is_acc(self, acc):
        return acc in self.items
            
    
    def withdraw(self,acc, money):
        acc= acc.upper()
        if self.is_acc(acc):
            if self.items[acc] >= money:
                self.items[acc] -= money
                print(f'you withdraw Rs.{money} from A/c No {acc}')
                print(f'Your current balance is {self.items[acc]}\n')
            else:
                print('Insufficient Fund\n')
            
        else:
            print('A/c not Exist\n')
            
        
    def check_balance(self, acc):
        acc= acc.upper()
        if self.is_acc(acc):
            print(f'Your account balance is {self.items[acc]}\n')
        else:
            print('Not Exist in our DataBase\n')
            
        
sbi = Bank()

sbi.Create_Account('SB-12', 100)
sbi.Create_Account('SB-12', 1050)
sbi.Create_Account('SB-15', 5050)
sbi.Create_Account('SB-20', 2450)

sbi.Customers_Details()

sbi.withdraw('sb-12', 500)

sbi.check_balance('sb-15')
sbi.check_balance('Sb-12')



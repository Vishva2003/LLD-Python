'''Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
'''
'''

dict={ a/c : [opendate , balance , name]}


'''
from datetime import date
import random

class Bank:
    def __init__(self):
        self.accounts ={}
        
    def opening_date(self):
        opening_date = date.today().strftime('%Y/%m/%d')
        return opening_date       
        
    def add_account(self,acc,customer_name ,balance ):
        details=[self.opening_date(), balance, customer_name]
        self.accounts[acc]= details
        print(f'Your A/C No is {acc}')
        print(f'Opening Date:{self.accounts[acc][0]} || Customer Name: {self.accounts[acc][2]} || Balance: {self.accounts[acc][1]}\n')
        
    def Print_bank_accounts(self):
        print('-------Bank Accounts---------')
        print('A/c No      Name        Balance     Opening Date')
        for accno , lis in self.accounts.items():

            print(f'{accno}      {lis[2]}      {lis[1]}      {lis[0]}')
        print()
        
    def is_account(self,accno):
        return accno in self.accounts
        
    def withdraw(self,accno, money):
        if self.is_account(accno):
            balance = self.accounts[accno][1]
            if money <= balance:
                self.accounts[accno][1]-= money
                print(f'Withdraw:{balance - money}  Balance:{self.accounts[accno][1]}')
            else:
                print('Insufficient Balance\n')
        else:
            print('Invalid Info\n')
            
    def deposite(self, accno, money):
        if self.is_account(accno):
            self.accounts[accno][1]+=money
            print(f'Deposite:{money}  Balance: {self.accounts[accno][1]}\n')
        else:
            print('A/c Not exist\n')
            
    
    def balance(self,acc):
        if self.is_account(acc):
            print(f'A/c no : {acc} Balance: {self.accounts[acc][1]}\n')
        else:
            print('A/c not Exist\n')
    
visgo = Bank()

visgo.add_account(3454,'vishva',1000)
visgo.add_account(1234,'vishv',1000)

visgo.Print_bank_accounts()

visgo.withdraw(1234, 300)

visgo.deposite(3454, 500)

visgo.balance(3454)
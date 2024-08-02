''''Write a Python program to create a calculator class. Include methods for basic arithmetic operations.'''

class Calculator:
        
    
    def add(self,num1,num2):
        self.n1=num1
        self.n2=num2
        return self.n1 + self.n2
    
    def sub(self,num1,num2):
        self.n1=num1
        self.n2=num2
        return self.n1 - self.n2

    def mul(self,num1,num2):
        self.n1=num1
        self.n2=num2
        return self.n1 * self.n2
    
    def div(self,num1,num2):
        self.n1=num1
        self.n2=num2
        if self.n2==0:
            return ('Cannot divide by zero.')
        return self.n1 / self.n2
    
    def mod(self,num1,num2):
        self.n1=num1
        self.n2=num2
        return self.n1 % self.n2

calci=Calculator()
print( calci.add(3,4))
print( calci.sub(3,4))
print( calci.mul(3,4))
print( calci.div(3,0))
"""Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
"""
"""  
lis=[]
stack.pop
stack.push

"""


class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self, item):
        self.items.append(item)
        
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items)==0
        
    def pop(self, item):
        
        if item in self.items:
            indx = self.items.index(item)
            self.items.pop(indx)
            return self.items
        else:
            return 'Not Found'
        
    def stack(self):
        return self.items
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack Empty'
        
stack1= Stack()
stack1.push(1)
stack1.push(2)
stack1.push(2)
stack1.push(2)
stack1.push(2)
stack1.push(3)
print(stack1.pop(3))
print(stack1.size())
print(stack1.peek())
print(stack1.stack())


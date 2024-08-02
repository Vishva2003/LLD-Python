'''Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
'''

'''

list=[]
enque
dequeue

'''

class Queue:
    
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items) == 0 
        
    def enqueue(self, item):
        self.items.append(item)
        print(f'{item} is added to queue')
        
    def dequeue(self):
        if not self.is_empty():
            print(f'{self.items[0]} is removed from queue')
            self.items.pop(0)
            
            
        else:
            raise IndexError('Cannot Dequeue for queue')
        
    def list_item(self):
        return f'Queue:   {self.items}'
            
            
        

queue = Queue()
queue.enqueue(10)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print(queue.list_item())

queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.list_item())




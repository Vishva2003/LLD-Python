from collections import Counter

class vehicle:
    def __init__(self,name, max_speed ,milage , capacity):
        self.name =name
        self.max_speed = max_speed
        self.milage=milage
        self.seat_capacity= capacity
    
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.seat_capacity} passengers"
 
    def fare(self):
        return self.seat_capacity*100

class Bus(vehicle):
    color = 'White'
    def fare(self):
        amount=super().fare()
        amount+= amount*(10/100)
        return amount
    
class Car(vehicle):
    color = 'Red'
        
Bus1 = Bus("School Volvo", 180, 12 , 50)
print("Total Bus fare is:", Bus1.fare())


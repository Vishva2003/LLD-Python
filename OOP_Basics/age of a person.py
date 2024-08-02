'''Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.'''

from datetime import date

class Person:
  def __init__(self, name , country , dob):
    self.name=name
    self.country = country
    self.dob=dob.split('-')
  
  
  def age(self):
    Today= date.today()
    Dob_list=[int(item) for item in self.dob]
    DOB = date(Dob_list[2], Dob_list[1],Dob_list[0])
    age= Today.year -DOB.year
    
    if (Today.month, Today.day) < (DOB.month, DOB.year):
      age-+1
      
    return age


person1=Person("Ferdi Odilia", "France", '15-5-2003')

person1.age().Today

print(f'Name: {person1.name} Country: {person1.country} Age: {person1.age()}')
    
    
'''Write a Python program to create a class that represents a shape. 
Include methods to calculate its area and perimeter. Implement subclasses 
for different shapes like circle, triangle, and square.'''
import math

class Shape:
    
    def Area(self):
        pass
    
    def Perimeter(self):
        pass


class Circle(Shape):
    
    def __init__(self, radius):
        self.R = radius
        
        
    def Area(self):
        return int(math.pi * (self.R**2))
    
    def Perimeter(self):
        return int(2* math.pi *self.R)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.L=length
        self.W = width
        
    def Area(self):
        return self.L * self.W

    def Perimeter(self):
        return 2* self.L + 2*self.W

class Square(Shape):
    def __init__(self, side):
        self.S =side
        
    def Area(self):
        return self.S**2

    def Perimeter(self):
        return 4* self.S

class Triange(Shape):
        
    def Area(self ,L,W):
        self.L = L
        self.W = W
        return 0.5 *self.L * self.W

    def Perimeter(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        return self.s1 + self.s2 + self.s3
    
triangle= Triange()
print(triangle.Area(2,3) , triangle.Perimeter(2,3,4))

circle = Circle(4)
print(circle.Area(), circle.Perimeter())

rectangle = Rectangle(4,5)
print(rectangle.Area(), rectangle.Perimeter())

square = Square(5)
print(square.Area(), square.Perimeter())
"""class Area:

    def circle(self,R):
        return int(math.pi * (R**2))
    
    def triangle(self, B, H):
        return 0.5* B*H
    
    def square(self, side):
        return side*side
    

class Perimeter:
    def circle(self,R):
        return 2* math.pi *R
    
    def triangle(self, s1, s2, s3):
        return s1+s2+s3
    
    def square(self, side):
        return 4*side
        
        
area=Area()      
print(area.circle(3))
print(area.square(3))
print(area.triangle(3,4))"""
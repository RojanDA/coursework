#Write a program that defines a method in the base class Shape and 
# overrides it in the derived classes Circle and Rectangle to 
# calculate the area.
import math
class shape:
    def area(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi* self.radius**2

class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
circle = Circle(6)
rectangle = Rectangle(5,6)


print("area of circle is ", circle.area())
print("area of circle is ", rectangle.area())
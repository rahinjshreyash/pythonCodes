# (AUTOMATED GEOMECTRIC CALCULATIONS)
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def circumference(self):
        return 2* math.pi*radius
    
while True:
     radius = float(input('enter the radius :'))

     circle = Circle(radius)
     print('Area of the circle is',circle.area())
     print('Circumference of the circle is',circle.circumference())
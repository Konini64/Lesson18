print("#C01")
class Apple:
    def __init__(self,w,c,t,b):
        self.weight = w
        self.color  = c
        self.taste  = t
        self.birth  = b
        print("Created!")

print("#C02")
import math
class Circle:
    def __init__(self,r):
        self.range = r
        print("Created!")
    def area(self):
        return math.pi * self.range * self.range

circle = Circle(5)
print (circle.area())

print("#C03")
class Triangle:
    def __init__(self,b,h):
        self.bottom = b
        self.hight = h
        print("Created!")
    def area(self):
        return self.bottom * self.hight / 2

triangle = Triangle(10,5)
print (triangle.area())

print("#C04")

class Hexagon:
    def __init__(self,a,b,c,d,e,f):
        self.hen1 = a
        self.hen2 = b
        self.hen3 = c
        self.hen4 = d
        self.hen5 = e
        self.hen6 = f
        print("Created!")
    def calculate_perimeter(self):
        return self.hen1 + self.hen2 + self.hen3 + self.hen4 + self.hen5 + self.hen6

hexagon = Hexagon(10,11,12,13,14,15)
print (hexagon.calculate_perimeter())











"""
class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color  = c
        print("Created!")

or1 = Orange(10,"dark orange")
or2 = Orange(18,"light orange")

print(or1)
print(or2)

or1.weight = 100
or2.color  = "red orange"

print(or1.weight)
print(or2.color)
class Orange:
    def __init__(self,w,c):
        #weight is gram
        self.weight = w
        self.color  = c
        self.mold = 0
        print("Created!")
    def rot(self,days,temp):
        #temp is c
        self.mold = days * temp

orange = Orange(200,"orange")
print(orange.mold)
orange.rot(10,37)
print(orange.mold)

class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def area(self):
        return self.width * self.len
    def change_size(self,w,l):
        self.width = w
        self.len = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())

"""

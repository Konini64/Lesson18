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
"""

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


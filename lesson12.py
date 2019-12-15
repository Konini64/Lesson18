"""
class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len   = l
    def area(self):
        return self.width * self.len

rectangle = Rectangle(12,10)
#print(rectangle.area())

class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]
    def change_data(self,index,n):
        self.nums[index] = n

data1 = Data()
data2 = Data()

data1.change_data(2,9)
data2.nums[2] = 9
print (data1.nums)
print (data2.nums)
print(type("HELLO"))
print(type(200))
print(type(200.2))
print(type(True))

class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len   = l
    def print_size(self):
        print("{} by {}".format(self.width,self.len))

myshape = Shape(20,25)
myshape.print_size()

class Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(20,20)
print(a_square.area())

class Triangle(Square):
    def area(self):
        return int(self.width * self.len / 2)

a_triangle = Triangle(20,20)
print(a_triangle.area())
"""
class Dog:
    def __init__(self,name,breed,owner):
        self.name  = name
        self.breed = breed
        self.owner = owner
class person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

mick = person ("Micky Mouse",456)
stan = Dog("Broot","Pug", mick)
print(stan.owner.age)



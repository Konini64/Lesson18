print("C01")
class Shape:
    def __init__(self):
        self.iam = "shape"
    def what_am_i(self):
        print ("I am a {}".format(self.iam))

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len   = l
        self.iam = "rectangle"
    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self,l):
        self.len   = l
        self.iam = "square"
    def calculate_perimeter(self):
        return self.len * 4
    def change_size(self,c_l):
        self.t = self.len + c_l
        if self.t <= 0:
            print("wrong data :" + str(self.t))
        else:
            self.len = self.t




rectangle = Rectangle(10,40)
list_r = ["rectangle",rectangle.width,rectangle.len,rectangle.calculate_perimeter()]
print(list_r)

square = Square(5)
list_s = ["square",square.len,square.calculate_perimeter()]
print(list_s)

print("C02")
square.change_size(5)
list_s = ["square","C +5",square.len,square.calculate_perimeter()]
print(list_s)
square.change_size(-5)
list_s = ["square","C -5",square.len,square.calculate_perimeter()]
print(list_s)
square.change_size(-10)
list_s = ["square","C -10",square.len,square.calculate_perimeter()]
print(list_s)

print("C03")
shape = Shape()
shape.what_am_i()
rectangle.what_am_i()
square.what_am_i()



print("C04")
class Horse:
    def __init__(self,name,breed,rider):
        self.name  = name
        self.breed = breed
        self.rider = rider
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

take = Person ("Yutaka Take",50)
oguri = Horse("Oguricap","ashige", take)
print(oguri.name + "'s rider is " + oguri.rider.name + " only.")

#sample
print("S_C01-------------------------------------------------")
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

print("S_C02")
class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

print("S_C03")
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

print("S_C04")
class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Harry")
the_rider = Rider("Sally", harry_the_horse)

print(the_rider.horse.name)

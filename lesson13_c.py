
class Square():
    square_list = []
    def __init__(self,l,name):
        self.len   = l
        self.iam = "square"
        self.name = name
        #self.square_list.append(self.name)
    def calculate_perimeter(self):
        return self.len * 4
    def change_size(self,c_l):
        self.t = self.len + c_l
        if self.t <= 0:
            print("wrong data :" + str(self.t))
        else:
            self.len = self.t
    def __repr__(self):
        return (str(self.len) + " by " + str(self.len) + " by " + str(self.len) + " by " + str(self.len))


s1 = Square(10,"s1")
s2 = Square(10,"s2")
s3 = Square(10,"s3")
s4 = Square(10,"s4")

#print (Square.square_list)

print(s1)

def comp (a,b):
    return a is b

print (comp(s1,s2))

print (comp(s1,s1))

a,b = input(), input()

#再帰関数
def gcd(a, b):
    if b == 0:
        #print (a)
        return a
    else:
        #print (a)
        return gcd(int(b), int(a)%int(b))
#print("end")
print(gcd(a,b))
print("---")
print(int((int(a)*int(b))/gcd(a,b)))


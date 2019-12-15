path = 'data/test.txt'
C_Q = set()
with open(path) as f:
    while True:
        s = f.readline()
        if s != "":
            z = int(s.strip("\n"))
            C_Q.add(z)
        else:
            break
print ("-----")

print (C_Q)
SC_Q = sorted(C_Q,reverse=True)
print (SC_Q)

print ("-----")
x = len(SC_Q)
y = 0
while y < x:
    print(SC_Q[y])
    y += 1

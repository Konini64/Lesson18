import math
x = 10000
a = range(x)
for p in a:
    if not p:
        continue
    elif p > math.sqrt(x):
        break
    else:
        for multi in range(p+p, 10000, p):
            a[multi] = 0
a = [x for x in a if x]
for x in a: print (x)



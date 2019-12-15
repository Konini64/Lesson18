a,b = input(), input()
int_a = int(a)
int_b = int(b)
A_Q   = set()
B_Q   = set()
C_Q   = set()

for x in range(1,int_a):
    a_q,a_m = divmod(int_a,x)
    if a_m == 0:
      #print (a_q,a_m)
      A_Q.add(a_q)

print (A_Q)
SA_Q = sorted(A_Q)
print (SA_Q)


for x in range(1,int_b):
    b_q,b_m = divmod(int_b,x)
    if b_m == 0:
      #print (b_q,b_m)
      B_Q.add(b_q)

print (B_Q)
SB_Q = sorted(B_Q)
print (SB_Q)

C_Q = A_Q & B_Q

print (C_Q)
SC_Q = sorted(C_Q,reverse=True)
print (SC_Q)
print (SC_Q[0])

print("-----")
#print(b)

x = max(int_a,int_b)
y = min(int_a,int_b)

def gcd(int_a,int_b):
    x = max(int_a,int_b)
    y = min(int_a,int_b)
    while x%y != 0:
       z = x%y
       x = y
       y = z
    else:
        return gcd(b,x%y)
#print gcd(int_a,int_b)
print gcd(a,b)

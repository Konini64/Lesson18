def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True
#-----------------------------------------------
#import math
import sys
ondo = input ()
len_ondo = len(ondo)

print (str(len_ondo) + " is len_ondo")

pre_ondo = ondo[0:len_ondo - 1]

print (str(pre_ondo) + " is pre_ondo")

if is_num(pre_ondo) == False:
    print (str(pre_ondo) + " is not decimal")
    sys.exit
else:
    flt_ondo = float(pre_ondo)
    print (str(flt_ondo) + " is flt_ondo")

aft_ondo = ondo[len_ondo - 1:len_ondo]

if aft_ondo == "F":
    res_ondo = (flt_ondo - 32 ) * (5/9)
    print ( str(res_ondo) + "C")
elif aft_ondo == "C":
    res_ondo = flt_ondo  *  (9/5) + 32 
    print ( str(res_ondo) + "F")
else:
    print (aft_ondo + " is not invalid")
    sys.exit

import re
r = re.compile(r'^([\.\d]+)(C|F)$', re.I)
t = input('temperature(C or F)= (ex 5C, 41F, etc)? ')
q = r.match(t)
if q:
    if q.group(2).upper() == 'C':
        print ('%fF' % (float(q.group(1)) * 9 / 5 + 32))
        if q.group(2).upper() == 'F':
            print ('%fC' % ((float(q.group(1)) - 32) * 5 / 9))

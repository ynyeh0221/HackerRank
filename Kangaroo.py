import sys

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if (x1 > x2 and v1 >= v2) or (x1 < x2 and v1 <= v2) or abs(x1-x2) % abs(v1-v2) != 0:
    print 'NO'
else:
    print 'YES'

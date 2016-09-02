import sys

N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))
res = 0;
for i in xrange(N-1):
    if B[i] % 2 == 1:
        B[i] += 1
        B[i+1] += 1
        res += 2;    
if B[-1] % 2 == 1: 
    print 'NO'
else:
    print res

import sys

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    res = 0
    print_res = False
    for i in xrange(n-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print "Too chaotic"
            print_res = True
            break
        for j in xrange(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                res += 1
    if not print_res:
        print res

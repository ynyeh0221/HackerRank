T = int(raw_input())
for t in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    if n % 2 == 0:
        print 0
    else:
        res = 0
        for i in xrange(0, n, 2):
            res ^= a[i]
        print res  

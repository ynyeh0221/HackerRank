import sys
N = int(raw_input())
for nn in xrange(N):
    n = int(raw_input())
    A = map(int, raw_input().split())
    minn = min(A)
    res = sys.maxint
    for i in xrange(-5, 1):
        temp = 0
        for j in xrange(n):
            delta = A[j] - i - minn
            temp += delta/5 + delta%5/2 + delta%5%2
        res = min(temp, res)
    print res

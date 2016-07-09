T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    Y = sorted(map(int, raw_input().split(' ')))
    res = 0
    ind = 0
    i = 1
    while i <= N:
        if i == N or (i < N and Y[i] != Y[i-1]):
            res += ((N+1) * (i-ind))/float(N-ind+1)
            ind = i
        i += 1
    print "%.2f" % res  

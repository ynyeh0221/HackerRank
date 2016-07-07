# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    H = sorted(map(int, raw_input().split(' ')))
    for i in xrange(1,N):
        H[i] += H[i-1]
    res = H[N-1]
    for i in xrange(1, N):
        res = max(res, (i+1)*(H[N-1] - H[i-1]))
    print res

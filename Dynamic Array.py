# Enter your code here. Read input from STDIN. Print output to STDOUT
[N,Q] = map(int, raw_input().split())
seqList = [[] for i in xrange(N)]
lastAns = 0
for q in xrange(Q):
    [op,x,y] = map(int, raw_input().split())
    if op == 1:
        seqList[(x ^ lastAns) % N] += [y]
    else:
        s = seqList[(x ^ lastAns) % N]
        lastAns = s[y % len(s)]
        print lastAns

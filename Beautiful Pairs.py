N = int(raw_input())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
Aind = set([i for i in xrange(N)])
Bind = set([i for i in xrange(N)])
res = 0
for i in xrange(N):
    for j in xrange(N):
        if i in Aind and j in Bind:
            if A[i] == B[j]:
                res += 1
                Aind.remove(i)
                Bind.remove(j)
if len(Aind) > 0 and len(Bind) > 0:
    print res + 1
else:
    print res - 1

N = int(raw_input())
A = map(int, raw_input().split())
A = sorted(A)
found = False
for i in xrange(N-1,-1,-1):
    for j in xrange(i-1,-1,-1):
        for k in xrange(j-1,-1,-1):
            if A[j]+A[k] > A[i]:
                print ' '.join(str(e) for e in [A[k],A[j],A[i]])
                found = True
                break
        if found:
            break
    if found:
        break
if not found:
    print -1

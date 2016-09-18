N = int(raw_input())
A = map(int,raw_input().split())
B = map(int,raw_input().split())
minn = 3000
res = []
diff = {}
for i in xrange(len(A)):
    diff[A[i]] = i
for i in xrange(len(B)):
    diff[B[i]] = abs(i - diff[B[i]])
for k in diff:
    if diff[k] == minn:
        res += [k]
    elif diff[k] < minn:
        minn = diff[k]
        res = [k]
print min(res)

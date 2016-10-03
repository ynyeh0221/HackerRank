[N, K] = map(int, raw_input().split())
C = map(int, raw_input().split())
C = sorted(C, reverse = True)
res = count = x = 0
while True:
    for i in xrange(K):
        res += (x+1) * C[count]
        count += 1
        if count == N:
            break
    if count == N:
        break
    x += 1
print res

m = 10**9+7
T = int(raw_input())
for t in xrange(T):
    [M,N] = map(int, raw_input().split())
    X = map(int, raw_input().split())
    Y = map(int, raw_input().split())
    X = sorted(X, reverse = True)
    Y = sorted(Y, reverse = True)
    x = y = res = 0
    while x < M-1 and y < N-1:
        if X[x] > Y[y]:
            res += (X[x] * (y+1)) % m
            res %= m
            x += 1
        else:
            res += (Y[y] * (x+1)) % m
            res %= m
            y += 1
    while x < M-1:
        res += (X[x] * (y+1)) % m
        res %= m
        x += 1
    while y < N-1:
        res += (Y[y] * (x+1)) % m
        res %= m
        y += 1
    print res

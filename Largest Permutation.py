[N,K] = map(int, raw_input().split())
s = map(int, raw_input().split())
pos = [0 for i in xrange(N+1)]
for i in xrange(N):
    pos[s[i]] = i
for i in xrange(N, 0, -1):
    actual = pos[i]
    expect = N - i
    if actual != expect:
        pos[s[expect]] = actual
        s[actual] = s[expect]
        s[expect] = i
        K -= 1
        if K < 1:
            break
print ' '.join(str(e) for e in s)

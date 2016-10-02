[N,K] = map(int, raw_input().split())
important = []
res = 0
for i in xrange(N):
    s  = map(int, raw_input().split())
    if s[1] == 0:
        res += s[0]
    else:
        important += [s[0]]
important = sorted(important, reverse = True)
for i in xrange(len(important)):
    if i < K:
        res += important[i]
    else:
        res -= important[i]
print res

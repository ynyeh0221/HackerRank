T = int(raw_input())
for t in xrange(T):
    [N, M, S] = map(int, raw_input().split(' '))
    res = (S - 1 + M) % N
    if res != 0:
        print res
    else:
        print N

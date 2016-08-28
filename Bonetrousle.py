def find(n, k, b):
    if n > (k-b+1 + k) * b / 2:
        print -1
        return
    res = [n / b for i in xrange(b)]
    for i in xrange(b/2):
        res[i] -= b/2 - i
    for i in xrange(b/2, b):
        res[i] += i - b/2
    diff = n - sum(res)
    while diff > 0:
        for i in xrange(b-1,-1,-1):
            if diff == 0:
                break
            res[i] += 1
            if res[i] > k:
                print -1
                return
            diff -= 1
    for i in xrange(1, len(res)):
        if res[i] == res[i-1]:
            print -1
            return
    print ' '.join(str(e) for e in res) if res[0] >= 1 else -1
        
t = int(raw_input())
for tt in xrange(t):
    s = map(int, raw_input().split(' '))
    n = s[0]
    k = s[1]
    b = s[2]
    find(n, k, b)        

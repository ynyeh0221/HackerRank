length = int(raw_input())
s = raw_input()
n = length / 4
A = T = G = C = 0
for i in s:
    if i == 'A':
        A += 1
    elif i == 'T':
        T += 1
    elif i == 'G':
        G += 1
    else:
        C += 1
res = 0
if A != n or C != n or G != n or T != n:
    res = length + 1
    l = 0
    for r in xrange(length):
        if s[r] == 'A':
            A -= 1
        if s[r] == 'T':
            T -= 1
        if s[r] == 'G':
            G -= 1
        if s[r] == 'C':
            C -= 1
        while A <= n and C <= n and G <= n and T <= n and l <= r:
            res = min(res, r - l + 1)
            if s[l] == 'A':
                A += 1
            if s[l] == 'T':
                T += 1
            if s[l] == 'G':
                G += 1
            if s[l] == 'C':
                C += 1
            l += 1
print res

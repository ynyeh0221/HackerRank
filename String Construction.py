import sys

n = int(raw_input().strip())
for a0 in xrange(n):
    s = raw_input().strip()
    pset = set()
    p = ''
    res = 0
    for i in s:
        if i not in pset:
            res += 1
            pset.add(i)
    print res

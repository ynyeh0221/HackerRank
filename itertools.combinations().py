import itertools
[s, k] = raw_input().split()
k = int(k)
for i in xrange(1,k+1):
    temp = []
    for j in itertools.combinations(s, i):
        temp += [''.join(sorted(j))]
    for j in sorted(temp):
        print j

import itertools
[s, k] = raw_input().split()
k = int(k)
res = []
for i in itertools.combinations_with_replacement(s, k):
    res += [''.join(sorted(i))]
for i in sorted(res):
    print i

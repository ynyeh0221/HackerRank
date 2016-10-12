import itertools
[s, k] = raw_input().split()
k = int(k)
res = []
for i in itertools.permutations(s, k):
    res += [''.join(i)]
for i in sorted(res):
    print i

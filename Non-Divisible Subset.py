[n, k] = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))
mod = [0 for i in xrange(k)]
for i in a:
    mod[i % k] += 1
res = 0
if k % 2 == 0:
    mod[k/2] = min(1, mod[k/2])
for i in xrange(1, k/2+1):
    res += max(mod[i], mod[k-i])
res += min(1, mod[0])
print res

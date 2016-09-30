# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input()
b = raw_input()
aa = int(a, 2)
bb = int(b, 2)
m = 10**9+7
res = 0
res += ((314160 - len(a)) * (aa % m)) % m
res += (((2 ** 314160 - 2 ** len(a)) % m) * (bb % m)) % m
res %= m

for i in xrange(len(a)):
    res += (aa ^ (bb << i)) % m
    res %= m
print res

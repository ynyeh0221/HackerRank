# Enter your code here. Read input from STDIN. Print output to STDOUT
[N, M] = map(int, raw_input().split())
s = 0
for m in xrange(M):
    [a, b, k] = map(int, raw_input().split())
    s += (b - a + 1) * k
print s / N

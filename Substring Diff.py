# O(N^3), timeout

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in xrange(T):
    s = raw_input().split(' ')
    S = int(s[0])
    s1 = s[1]
    s2 = s[2]
    n = len(s1)
    res = 0
    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            diff = 0
            for l in xrange(1, n+1):
                if i+l-1 <= n and j+l-1 <= n:
                    if s1[i+l-2] != s2[j+l-2]:
                        diff += 1
                        if diff > S:
                            break
                    res = max(res, l)
    print res

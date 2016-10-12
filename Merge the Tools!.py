s = raw_input()
n = len(s)
k = int(raw_input())
for i in xrange(0, n, k):
    dic = {}
    res = ""
    for c in s[i:i+k]:
        if c not in dic:
            dic[c] = 1
            res += c
    print res
